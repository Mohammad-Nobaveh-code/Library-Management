from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import CustomUser


class LoginForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def cleand_password2(self):
		if self.cleaned_data['password'] != self.cleaned_data['password2']:
			raise forms.ValidationError('passwords are not match!')
		return self.cleaned_data['password2']


class ContactForm(forms.Form):
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=150)
	message = forms.CharField(widget=forms.Textarea, max_length=2000)

