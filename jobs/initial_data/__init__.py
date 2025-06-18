"""Initial data required for core sites."""
import os
from nautobot.apps.jobs import register_jobs, IntegerVar

from nautobot_design_builder.design_job import DesignJob
from nautobot_design_builder.choices import DesignModeChoices

from .context import InitialDesignContext

current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, "README.md"), "r") as docs:
    docs_data = docs.read()

class InitialDesign(DesignJob):
    """Initialize the database with default values needed by the core site designs."""

    has_sensitive_variables = False
    routers_per_site = IntegerVar(min_value=1, max_value=8, default=2)

    class Meta:
        """Metadata needed to implement the backbone site design."""

        design_mode = DesignModeChoices.DEPLOYMENT
        name = "Initial Data"
        commit_default = False
        design_file = "designs/0001_design.yaml.j2"
        context_class = InitialDesignContext
        version = "1.0.0"
        description = "Establish the devices and site information for four sites: IAD5, LGA1, LAX11, SEA11."
        docs = docs_data


name = "Demo Designs"
register_jobs(InitialDesign)
