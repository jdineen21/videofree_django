from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'text_input',
            'placeholder': 'Username',
        })
    )
    first_name = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'text_input',
            'placeholder': 'First name',
        })
    )
    second_name = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'text_input',
            'placeholder': 'Second name',
        })
    )
    email = forms.CharField(
        label='',
        max_length=20,
        widget=forms.EmailInput(attrs={
            'class': 'text_input',
            'placeholder': 'Email address',
        })
    )
    password = forms.CharField(
        label='',
        max_length=20,
        widget=forms.PasswordInput(attrs={
            'class': 'text_input',
            'placeholder': 'Password',
        })
    ) 