"""
This code is based on the source code of the django-survey application
by Pierre Sassoulas, 2022, version 1.4.0. 
Available at https://github.com/Pierre-Sassoulas/django-survey
"""

from abc import update_abstractmethods
# Import geographic model since we will be saving location data
from django.contrib.gis.db import models
from .response import Response
from .question import Question
from django.utils.translation import gettext_lazy as _

# Represents a single answer given to a certain question as part of a user's response
class Answer(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(_("Creation date"))
    updated = models.DateTimeField(_("Last edited"))
    body = models.TextField(_("Answer Body"))
    lon = models.FloatField()
    lat = models.FloatField()
    