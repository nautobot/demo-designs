"""This module contains the render context for the basic design."""

from django.core.exceptions import ObjectDoesNotExist

from nautobot_design_builder.errors import DesignValidationError
from nautobot_design_builder.context import Context, context_file

from nautobot.dcim.models import Location
from nautobot.extras.models import Role, Tag
from nautobot.ipam.models import Prefix, VLAN

BRANCH_SUPERNET_PREFIXLEN = 21
APPLICATION_SUPERNET_PREFIXLEN = 27

@context_file("context.yaml")
class BaseDataContext(Context):
    """Render context for base data."""

@context_file("context.yaml")
class NewApplicationDesignContext(Context):
    """Render context for application design."""

    def get_next_vlans(self):
        """Get next available VLAN ID."""
        used_vlans = VLAN.objects.values_list("vid", flat=True)
        for vid in range(2001, 2998):
            if (vid not in used_vlans) and (vid + 1 not in used_vlans) and (vid + 2 not in used_vlans):
                return {"web": str(vid), "app": str(vid + 1), "db": str(vid + 2)}
        raise DesignValidationError("No available consequtive VLAN IDs in the range 2001-2999!")

    def application_vlans(self):
        """Get or create application VLAN."""
        application_vlans = {}
        for tier in ["web", "app", "db"]:
            try:
                application_vlans[tier] = str(VLAN.objects.get(name=f"{self.app_name}-{tier}").vid)
            except ObjectDoesNotExist:
                application_vlans = self.get_next_vlans()
        return application_vlans

    def get_next_prefix(self):
        """Get next available prefix."""
        base_prefix = Prefix.objects.get(prefix=self.base_prefix)
        available_prefixes = base_prefix.get_available_prefixes().iter_cidrs()
        filtered_available_prefixes = [p for p in available_prefixes if p.prefixlen <= APPLICATION_SUPERNET_PREFIXLEN]
        try:
            container = sorted(filtered_available_prefixes, reverse=True, key=lambda x: x.prefixlen)[0]
            return str(container.network) + "/" + str(APPLICATION_SUPERNET_PREFIXLEN) 
        except IndexError:
            raise DesignValidationError("Not enough IP space to create new branch!")

    def application_supernet(self):
        """Get or create application supernet."""
        try:
            location = Location.objects.get(name=self.pod.name)
            role = Role.objects.get(name="Application:Supernet")
            tag = Tag.objects.get(name=self.app_name)
            return str(Prefix.objects.get(location=location, role=role, tags=tag))
        except ObjectDoesNotExist:
            return self.get_next_prefix()

@context_file("context.yaml")
class NewPodDesignContext(Context):
    """Render context for pod design."""

    def get_next_prefix(self):
        """Get next available prefix."""
        base_prefix = Prefix.objects.get(prefix=self.base_prefix)
        available_prefixes = base_prefix.get_available_prefixes().iter_cidrs()
        filtered_available_prefixes = [p for p in available_prefixes if p.prefixlen <= BRANCH_SUPERNET_PREFIXLEN]
        try:
            container = sorted(filtered_available_prefixes, reverse=True, key=lambda x: x.prefixlen)[0]
            return str(container.network) + "/" + str(BRANCH_SUPERNET_PREFIXLEN) 
        except IndexError:
            raise DesignValidationError("Not enough IP space to create new branch!")
            

    @property
    def branch_supernet(self):
        """Calculate the branch prefixes."""
        try:
            location = Location.objects.get(name=self.pod_name)
            return str(Prefix.objects.get(location=location, role__name="Branch:Supernet"))
        except ObjectDoesNotExist:
            return self.get_next_prefix()