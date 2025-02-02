from django import forms

class InputForm(forms.Form):
	text = forms.CharField(label="Enter Text", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
