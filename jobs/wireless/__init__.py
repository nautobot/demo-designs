"""Initial data required for controllers."""
from nautobot.apps.jobs import register_jobs

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

name = "Nautobot Demo Designs"
register_jobs(WirelessDesign)
