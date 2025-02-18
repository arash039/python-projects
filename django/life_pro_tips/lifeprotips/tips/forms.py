from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Tip
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class RegistrationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
	pass

class TipForm(forms.ModelForm):
	class Meta:
		model = Tip
		fields = ['content']
		widgets = {'content': forms.Textarea(attrs={'class': 'form-control', 'rows' : 3, 'placeholder' : 'Share your tip ...'}),}