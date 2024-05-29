"""The __init__.py module is required for Nautobot to load the jobs via Git."""

from .core_site import CoreSiteDesign
from .edge_site import EdgeDesign
from .initial_data import InitialDesign
from .p2p import P2PDesign

__all__ = [
    "CoreSiteDesign",
    "EdgeDesign",
    "InitialDesign",
    "P2PDesign",
]
