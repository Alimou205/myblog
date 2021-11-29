from django import forms
from django.forms.widgets import TextInput
from .models import Comment
class CommentForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Comment
        fields =['username','email','body']