from django.contrib.gis.db.models  import PointField, PolygonField, LineStringField

from django.db import models
from django.utils.translation import gettext_lazy as _
from .question import Question
from .answer import Answer

class Location(models.Model):
    """
    Abstract class for representing geographic locations of
    Questions and Answers.

    Attributes:
    - name: name for the location
    - question: a location may belong to a question
    - answer: a location may belong to an answer
    """
    name = models.CharField(max_length=100, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        "Returs the name of the location"
        return str(self.name)


class PointLocation(Location):
    """
    Represents the location of a question or answer as a POINT
    """
    location = PointField()


class PolygonLocation(Location):
    """
    Represents the location of a question or answer as a POLYGON
    """
    location = PolygonField()


class LineStringLocation(Location):
    """
    Represents the location of a question or answer as a LINESTRING
    """
    location = LineStringField()
