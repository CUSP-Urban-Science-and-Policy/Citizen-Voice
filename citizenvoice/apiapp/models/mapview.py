from django.db import models
from django.utils.translation import gettext_lazy as _

class MapView(models.Model):
    """
    The MapView class provides additional configuration settings for the Question class, and supports
    different map services and service agnostic map options.
    """
    map_service_url = models.CharField(_("Map Service URL"), max_length=150)
    options = models.JSONField()
