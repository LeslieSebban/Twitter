from django import forms
from django.contrib.auth.models import User
from twitter_app.models import UserProfileInfo

class UserFor(forms.ModelForm):
	password = forms.Charfield(widget = forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 'email', 'password') #tuple, car unique value


class UserProfileInfoForm(forms.ModelForm):
	
	class Meta():
		model = UserProfileInfo
		fields = ('bio', 'profile_pic')



class TweetForm (forms.Form):
	text = forms.Charfield(max_length=140, widget = forms.Textarea)
