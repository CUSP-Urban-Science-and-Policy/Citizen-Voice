"""
This code is based on the source code of the django-survey application
by Pierre Sassoulas, 2022, version 1.4.0. 
Available at https://github.com/Pierre-Sassoulas/django-survey
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from .survey import Survey

# Represents a single question of any type
class Question(models.Model):
    """
    The Question class allows for creating questions of several different types. It also includes the possibility
    to include potential answers as part of the question. These possible answers are not objects, but rather 
    captured in a comma-separated text field.
    """

    TEXT = "text"
    SHORT_TEXT = "short-text"
    RADIO = "radio"
    SELECT = "select"
    SELECT_IMAGE = "select_image"
    SELECT_MULTIPLE = "select-multiple"
    INTEGER = "integer"
    FLOAT = "float"
    DATE = "date"
    GEOSPATIAL = "geospatial"

    QUESTION_TYPES = (
        (TEXT, _("text (multiple line)")),
        (SHORT_TEXT, _("short text (one line)")),
        (RADIO, _("radio")),
        (SELECT, _("select")),
        (SELECT_MULTIPLE, _("Select Multiple")),
        (SELECT_IMAGE, _("Select Image")),
        (INTEGER, _("integer")),
        (FLOAT, _("float")),
        (DATE, _("date")),
        (GEOSPATIAL, _("geospatial"))
    )

    text = models.TextField(_("Text of the Question"))
    order = models.IntegerField(_("Order of where question is placed"))
    required = models.BooleanField(_("Question must be filled out"), default=False)
    question_type = models.CharField(_("Type of question"), max_length=150, choices=QUESTION_TYPES, default=TEXT)
    choices = models.TextField(_("Choices for answers"), blank=True, null=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")
        ordering = ("survey", "order")

