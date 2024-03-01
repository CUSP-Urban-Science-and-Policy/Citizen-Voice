"""
This code is based on the source code of the django-survey application
by Pierre Sassoulas, 2022, version 1.4.0. 
Available at https://github.com/Pierre-Sassoulas/django-survey
"""

import uuid
from django.db import models
from .survey import Survey
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Represents all the answers given by one user for the compiled set of questions
class Response(models.Model):
    """
    This class represents the collection of all answers by Respondent per survey. 
    Every Answer is thus linked to a response based on
    the respondent (user) that created the answer and for which survey.
    """
    
    created = models.DateTimeField(_("Date response was submitted"), auto_now_add=True)
    updated = models.DateTimeField(_("Last edit"), auto_now=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    interview_uuid = models.UUIDField (
        _("Unique ID of interview"),
        primary_key=True, 
        default=uuid.uuid4,
         max_length=150,
         unique=True
         )
    respondent = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Response {self.pk} ({self.survey.name})"
