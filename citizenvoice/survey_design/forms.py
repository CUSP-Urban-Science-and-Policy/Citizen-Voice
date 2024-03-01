from django import forms
from apiapp.models.survey import Survey


class SurveyCreationForm(forms.ModelForm):
    # def is_valid(self):

    class Meta:
        model = Survey
        fields = ['name', 'description', 'editable_answers']
