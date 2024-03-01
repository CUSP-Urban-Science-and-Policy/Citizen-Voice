from django.db import models
from django.utils.translation import gettext_lazy as _


def default_options():
    return {"zoom": 7, "center": [52.456009, 5.251465]}


def default_service_url():
    return "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"


class MapView(models.Model):
    """
    The MapView class provides additional configuration settings for the Question class, and supports
    different map services and service agnostic map options.
    """
    name = models.CharField(_("Name of the MapView location"), max_length=150, default="Delft")
    map_service_url = models.CharField(_("Map Service URL"), max_length=150,
                                       default=default_service_url)
    # TODO: add JSON validation to see if the data that is being stored is valid JSON
    options = models.JSONField(_("Map service specific options"), default=default_options)
    geometries = models.JSONField(_("Custom geometries for the map view"), blank=True, null=True) # TODO: [manuel] this should be a GeoJSONField, can DJANGO SUPPORT THIS? if not, we should do our own validation

    def __str__(self):
        return str(self.name)
