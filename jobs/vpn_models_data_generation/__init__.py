"""VPN Models data generation."""

from nautobot.apps.jobs import register_jobs
from nautobot_design_builder.contrib import ext
from nautobot_design_builder.design_job import DesignJob
from nautobot_design_builder.choices import DesignModeChoices
from .context import VPNModelsDataGenerationContext


class VPNModelsDataGeneration(DesignJob):
    """VPN Models data generation."""

    class Meta:
        """Metadata for the VPNModelsDataGeneration design."""

        name = "VPN Models data generation"
        description = "Generate VPN models data."
        nautobot_version = ">=2"
        has_sensitive_variables = False
        extensions = [ext.CableConnectionExtension]
        design_mode = DesignModeChoices.DEPLOYMENT
        design_files = [
            "designs/0000_vpn_datagen_dc.yaml.j2",
            "designs/1000_vpn_datagen_branches.yaml.j2",
        ]
        context_class = VPNModelsDataGenerationContext


register_jobs(VPNModelsDataGeneration)
