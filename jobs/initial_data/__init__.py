"""Initial data required for core sites."""

from nautobot.apps.jobs import register_jobs

from nautobot_design_builder.design_job import DesignJob
from nautobot.extras.jobs import IntegerVar

from .context import InitialDesignContext


class InitialDesign(DesignJob):
    """Initialize the database with default values needed by the core site designs."""

    has_sensitive_variables = False
    routers_per_site = IntegerVar(min_value=1, max_value=6, default=2)

    class Meta:
        """Metadata needed to implement the backbone site design."""

        name = "Initial Data"
        commit_default = False
        design_file = "designs/0001_design.yaml.j2"
        context_class = InitialDesignContext
        version = "1.0.0"
        description = "Establish the devices and site information for four sites: IAD5, LGA1, LAX11, SEA11."
        docs = """This design creates the following objects in the source of truth to establish the initia network environment in  four sites: IAD5, LGA1, LAX11, SEA11.

These sites belong to the America region (and different subregions), and use Juniper PTX10016 devices.

The user input data is:
    - Number of routers per site (integer)
    - The description for us-west-1 region (string)
"""


name = "Demo Designs"
register_jobs(InitialDesign)
