"""This module contains the render context for the non-network infra design."""

from nautobot_design_builder.context import Context, context_file


@context_file("context.yaml")
class NonNetworkDesignContext(Context):
    """Render context for non-network infra design."""
