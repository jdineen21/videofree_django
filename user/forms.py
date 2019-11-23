from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
        })
    )
    first_name = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'First name',
        })
    )
    second_name = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'Second name',
        })
    )
    email = forms.CharField(
        label='',
        max_length=20,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email address',
        })
    )
    password = forms.CharField(
        label='',
        max_length=20,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
        })
    )