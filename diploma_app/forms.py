from django import forms


class LoginForm(forms.Form):
    login = forms.CharField()
    passw = forms.CharField()
