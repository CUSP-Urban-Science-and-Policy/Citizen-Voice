from django import forms
from apiapp.models.response import Response
from apiapp.models.answer import Answer
from apiapp.models.location import PointFeature, PolygonFeature, LineFeature

class ResponseCreationForm(forms.ModelForm):
    """ModelForm child class for creating Response objects. Form does not include any field (fields are autofilled)"""

    class Meta:
        model = Response
        fields = []


class AnswerCreationForm(forms.ModelForm):
    """ModelForm child class for creating Answer objects. Form includes the field: body"""

    class Meta:
        model = Answer
        fields = ['body']
        # in case we want to have a label for the input area, we can
        labels = {
            'body': '',
        }

class PointLocationCreationForm(forms.ModelForm):
    """ModelForm child class for LocationPoint objects. Form does not include any field (fields are autofilled)"""

    class Meta:
        model = PointFeature
        fields = []

class PolygonLocationCreationForm(forms.ModelForm):
    """ModelForm child class for PolygonLocation objects. Form does not include any field (fields are autofilled)"""

    class Meta:
        model = PolygonFeature
        fields = []

class LineStringLocationCreationForm(forms.ModelForm):
    """ModelForm child class for LineStringLocation objects. Form does not include any field (fields are autofilled)"""

    class Meta:
        model = LineFeature
        fields = []

