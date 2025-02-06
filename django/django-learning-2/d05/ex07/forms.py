from django import forms
from .models import Movies

class UpdateForm(forms.Form):
	movie = forms.ModelChoiceField(queryset=Movies.objects.all(), label="Select Movie")
	opening_crawl = forms.CharField(widget=forms.Textarea, label="New Opening Crawl")
