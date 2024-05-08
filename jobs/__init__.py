"""The __init__.py module is required for Nautobot to load the jobs via Git."""

from .core_site import CoreSiteDesign
from .edge_site import EdgeDesign
from .initial_data import InitialDesign
from .l3vpn import L3vpnDesign

__all__ = [
    "CoreSiteDesign",
    "EdgeDesign",
    "InitialDesign",
    "L3vpnDesign",
]
