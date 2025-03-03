"""
This code is based on the source code of the django-survey application
by Pierre Sassoulas, 2022, version 1.4.0. 
Available at https://github.com/Pierre-Sassoulas/django-survey
"""

# from abc import update_abstractmethods
# Import geographic model since we will be saving location data
# from django.contrib.gis.db import moßdels
from django.db import models
from .response import Response
from .question import Question
from .mapview import MapView
from django.utils.translation import gettext_lazy as _


# Represents a single answer given to a certain question as part of a user's response
class Answer(models.Model):
    """
    The type-specific Answer model uses a generic text field to allow for flexible
    field sizes to accommodate for different Question types. It also contains latitude
    and longitude fields to capture spatial answers.
    """
    response = models.ForeignKey(Response, to_field="response_id", on_delete=models.CASCADE) # this field is not inheriting data type. Must be uuid.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    mapview = models.ForeignKey(MapView, on_delete=models.SET_NULL, blank=True, null=True)
    created = models.DateTimeField(_("Creation date"), auto_now_add=True)
    updated = models.DateTimeField(_("Last edited"), auto_now=True)
    body = models.TextField(_("Answer Body"), blank=True)
    
    # TODO: [manuel] Shall we define types for answers?
 


    def __str__(self):
        return f"Response {self.response.pk}:{self.question.text}"
