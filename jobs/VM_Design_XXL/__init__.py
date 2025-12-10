"""XXL demo design demonstrates the capabilities of the Design Builder."""

from nautobot.apps.jobs import ChoiceVar, IntegerVar, ObjectVar, StringVar, register_jobs
from nautobot.dcim.models import Location
from nautobot.tenancy.models import Tenant
from nautobot_design_builder.choices import DesignModeChoices
from nautobot_design_builder.design_job import DesignJob

from .context import NonNetworkDesignContext


class VMXXLDesign(DesignJob):
    """An XXL-scale infra design for design builder."""

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
        default=30,
    )
    memory_per_vm = ChoiceVar(
        label="Memory per VM (GB)",
        choices=[
            ("2", "2 GB"),
            ("4", "4 GB"),
            ("8", "8 GB"),
            ("16", "16 GB"),
            ("32", "32 GB"),
        ],
        default="8",
        description="Amount of memory (in GB) to assign to each VM.",
    )

    class Meta:
        """Metadata describing this XXL infra design job."""

        design_mode = DesignModeChoices.DEPLOYMENT
        name = "VM XXL Infra Design"
        dryrun_default = True
        has_sensitive_variables = False
        design_file = "designs/0001_design.yaml.j2"
        context_class = NonNetworkDesignContext
        nautobot_version = ">=2"


name = "Demo Designs"
register_jobs(VMXXLDesign)
