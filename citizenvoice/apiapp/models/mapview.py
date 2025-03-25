from django.db import models
from django.utils.translation import gettext_lazy as _
from .location import LocationCollection


def default_options():
    return {"zoom": 15, "center": [51.9999518, 4.3641589]}

def default_service_url():
    return "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"


class MapView(models.Model):
    """
    The MapView class provides additional configuration settings for the Question class, and supports
    different map services and service agnostic map options.
    """
    name = models.CharField(_("Name of the MapView location"), max_length=150, blank=True, default="Delft")
    map_service_url = models.CharField(_("Map Service URL"), max_length=150, default=default_service_url)
    description = models.TextField(_("Description of the MapView"), max_length=200, blank=True, null=True)
    options = models.JSONField(_("Map service specific options"), default=default_options)
    location = models.ForeignKey(LocationCollection, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.name)
