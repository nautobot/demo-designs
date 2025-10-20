"""Initial data required for controllers."""
from nautobot.apps.jobs import register_jobs

from nautobot_design_builder.choices import DesignModeChoices
from nautobot_design_builder.design_job import DesignJob

from .context import WirelessDesignContext


class WirelessDesign(DesignJob):
    """Initialize the database with default values needed by the wireless designs."""
    has_sensitive_variables = False

    class Meta:
        """Metadata needed to implement the wireless design."""

        name = "Wireless Data"
        commit_default = False
        design_file = "designs/0001_design.yaml.j2"
        context_class = WirelessDesignContext
        has_sensitive_variables = False
        version = "1.0.0"
        design_mode = DesignModeChoices.DEPLOYMENT
        docs = """
        # Wireless Data

        This job will create initial data required for wireless designs.

        ## Requirements

        - Nautobot Design Builder must be installed and configured.
        - The design file **must** be present in the specified path.
        - Nautobot 2.4.0 or higher.
        """

name = "Nautobot Demo Designs"
register_jobs(WirelessDesign)
