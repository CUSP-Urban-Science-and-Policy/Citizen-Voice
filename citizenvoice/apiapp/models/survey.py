"""
This code is based on the source code of the django-survey application
by Pierre Sassoulas, 2022, version 1.4.0. 
Available at https://github.com/Pierre-Sassoulas/django-survey
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Represents all the responses from every respondent


class Survey(models.Model):
    """
    The Survey class represents a collection of questions that are to be answered by respondents.
    It also represents all the responses made by respondents (users) for this specific Survey. 
    """

    name = models.CharField(_("Name of the survey"), max_length=150)
    description = models.TextField(_("Description"), blank=True)
    is_published = models.BooleanField(_("Survey is visible and accessible to users"), default=False)
    need_logged_user = models.BooleanField(_("Only authenticated users have access to this survey"), default=False)
    editable_answers = models.BooleanField(_("Answers can be edited after submission"), default=True)
    publish_date = models.DateTimeField(_("Date that survey was made available"))
    expire_date = models.DateTimeField(_("Expiry date of survey"))
    public_url = models.CharField(_("Public URL"), max_length=255, blank=True) # TODO: [manuel] this should be auto-generated when chosen by the designer 
    designer = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.name)

    def question_count(self):
        return self.question_set.count()
