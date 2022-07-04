from django.contrib.auth.forms import UserCreationForm as SignUpForm
from django import forms


class UserCreationForm(SignUpForm):
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta(SignUpForm.Meta):
        fields = ("username", "email")
