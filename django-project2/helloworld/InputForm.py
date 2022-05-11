from django import forms


class InputForm(forms.Form):
    firstName = forms.CharField(max_length=200)
    lastName = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())
