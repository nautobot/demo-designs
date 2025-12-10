"""Small/medium demo design demonstrates the capabilities of the Design Builder."""

from nautobot.apps.jobs import IntegerVar, ObjectVar, StringVar, register_jobs
from nautobot.dcim.models import Location
from nautobot.tenancy.models import Tenant
from nautobot_design_builder.choices import DesignModeChoices
from nautobot_design_builder.design_job import DesignJob

from .context import NonNetworkDesignContext


class VMSMDesign(DesignJob):
    """A basic small/medium infra design for design builder."""

    region = ObjectVar(
        label="Region",
        description="Select the region for this site",
        model=Location,
    )
    site_name = StringVar(
        label="Site Name",
        regex=r"\w{3}\d+",
        description="Unique name for the site.",
    )
    cluster_name = StringVar(
        label="Cluster Name",
        default="Cluster-01",
    )
    tenant = ObjectVar(
        label="Tenant",
        model=Tenant,
        required=False,
        description="Optional tenant to assign resources to.",
    )
    rack_name = StringVar(
        label="Rack Name",
        default="Rack-01",
    )
    vm_quantity = IntegerVar(
        label="Number of VMs",
        default=3,
    )

    class Meta:
        """Metadata describing this non-networking infra design job."""

        design_mode = DesignModeChoices.DEPLOYMENT
        name = "VM Small/Medium Infra Design"
        dryrun_default = True
        has_sensitive_variables = False
        design_file = "designs/0001_design.yaml.j2"
        context_class = NonNetworkDesignContext
        nautobot_version = ">=2"


name = "Demo Designs"
register_jobs(VMSMDesign)
