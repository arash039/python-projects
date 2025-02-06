from django import forms
from ex10.models import People

class CharacterFilterForm(forms.Form):
    min_release_date = forms.DateField(label="Movies minimum release date")
    max_release_date = forms.DateField(label="Movies maximum release date")
    planet_diameter = forms.IntegerField(label="Planet diameter greater than")
    gender = forms.ChoiceField(label="Character gender", choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gender'].choices = [
            (gender, gender) for gender in People.objects.values_list('gender', flat=True).distinct()
        ]