from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model ='User'
		fields =['username', 'email', 'password']

class resultForm(forms.ModelForm):
	user_name=forms.CharField()
	password=forms.CharField()
	total_score=forms.IntegerField()
	current_score=forms.IntegerField()
