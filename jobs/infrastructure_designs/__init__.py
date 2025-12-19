"""Basic design demonstrates the capabilities of the Design Builder."""

from nautobot.apps.jobs import register_jobs, StringVar, ObjectVar, BooleanVar

from nautobot.dcim.models import Location

from nautobot_design_builder.choices import DesignModeChoices
from nautobot_design_builder.contrib import ext
from nautobot_design_builder.design_job import DesignJob

from .context import BaseDataContext, NewApplicationDesignContext, NewPodDesignContext

name = "Infrastructure Designs"


class BaseData(DesignJob):
    """Load base data."""

    class Meta:
        """Metadata for the BaseData design."""

        name = "Base Data"
        description = "Load Nautobot base data."
        nautobot_version = ">=2"
        has_sensitive_variables = False
        design_file = "designs/0000_basedata.yaml.j2"
        context_class = BaseDataContext


class NewApplicationDesign(DesignJob):
    """A design to deploy a new application."""

    pod = ObjectVar(
        label="Pod",
        description="Pod for the new application",
        model=Location,
        query_params={"location_type": "Pod"},
    )
    app_name = StringVar(label="Application Name")

    class Meta:
        """Metadata describing this design job."""

        design_mode = DesignModeChoices.DEPLOYMENT
        deployment_name_field = "app_name"
        name = "New application"
        description = "Deploy a new application."
        version = "1.0"
        docs = "A design to deploy a new application."
        nautobot_version = ">=2"
        has_sensitive_variables = False
        extensions = [ext.NextPrefixExtension]
        design_file = "designs/0002_newapplication.yaml.j2"
        context_class = NewApplicationDesignContext


class NewPodDesign(DesignJob):
    """A design to deploy a new data center pod."""

    site = ObjectVar(
        label="Site",
        description="Site for the new rack",
        model=Location,
        query_params={"location_type": "Site"},
    )
    pod_name = StringVar(label="Pod Name", regex=r"\w{3}\d+")

    class Meta:
        """Metadata describing this design job."""

        design_mode = DesignModeChoices.DEPLOYMENT
        deployment_name_field = "pod_name"
        name = "New pod"
        description = "Create a new data center pod."
        version = "1.0"
        docs = "A design to deploy a new data center pod."
        nautobot_version = ">=2"
        has_sensitive_variables = False
        extensions = [ext.CableConnectionExtension, ext.NextPrefixExtension]
        design_file = "designs/0001_newpod.yaml.j2"
        context_class = NewPodDesignContext


register_jobs(BaseData, NewApplicationDesign, NewPodDesign)
