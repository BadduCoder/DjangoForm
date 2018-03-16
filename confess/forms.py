from django import forms
from .models import Confess

class Confessform(forms.ModelForm):
	to = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Confessing to?'}))
	message = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Message for him/her'}))
	class Meta:
		model = Confess
		fields = ('to','message',)