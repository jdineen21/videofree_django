
import string
import re

from django import forms

ALPHA_LOWER = string.ascii_lowercase
ALPHA_UPPER = string.ascii_uppercase
PUNCTUATION = string.punctuation

class SignupForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'text_input',
            'placeholder': 'Username',
        })
    )
    first_name = forms.CharField(
        label='',
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'text_input',
            'placeholder': 'First name',
        })
    )
    last_name = forms.CharField(
        label='',
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'text_input',
            'placeholder': 'Surname',
        })
    )
    email = forms.CharField(
        label='',
        max_length=100,
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'text_input',
            'placeholder': 'Email address',
        })
    )
    password = forms.CharField(
        label='',
        max_length=50,
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'text_input',
            'placeholder': 'Password',
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) == 0:
            raise forms.ValidationError('This field is required')
        if len(username) < 5:
            raise forms.ValidationError('This username is too short')
        if len(username) > 30:
            raise forms.ValidationError('This username is too long')
        if not username[0].isalnum() or not username[-1].isalnum():
            raise forms.ValidationError('First and last character must be alphanumeric')
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) == 0:
            raise forms.ValidationError('This field is required')
        if not first_name.isalpha():
            raise forms.ValidationError('Only letters are allowed in names')
        return first_name[0].upper() + first_name[1:]
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) == 0:
            raise forms.ValidationError('This field is required')
        if len(last_name) < 2:
            raise forms.ValidationError('This field must be at least 2 characters in length')
        if not last_name.isalpha():
            raise forms.ValidationError('Only letters are allowed in names')
        return last_name[0].upper() + last_name[1:]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if len(email) == 0:
            raise forms.ValidationError('This field is required')
        if not email.count('@') == 1:
            raise forms.ValidationError('Email must contain exactly 1 @ symbol')

        recipient_name = email[:email.find('@')]
        if len(recipient_name) == 0:
            raise forms.ValidationError('Email must be in format example@example.com')
        if len(recipient_name) > 64:
            raise forms.ValidationError('The recipient name may be a maximum of 64 characters long')
        
        # Domain length check
        # Domain symbol check
        full_domain = email[email.find('@')+1:]
        domain_levels = full_domain.split('.')
        for domain in domain_levels:
            if len(domain) == 0:
                raise forms.ValidationError('This email is not valid')

        return email
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if len(password) < 8:
            raise forms.ValidationError('This password is too short')
        if len(password) > 50:
            raise forms.ValidationError('This password is too long')
        if not re.search('[a-z]', password):
            raise forms.ValidationError('Password must container at least one lowercase letter')
        if not re.search('[A-Z]', password):
            raise forms.ValidationError('Password must container at least one lowercase letter')
        if not re.search('[0-9]', password):
            raise forms.ValidationError('Password must container at least one number')
        if not re.search('['+ PUNCTUATION +']', password):
            raise forms.ValidationError('Password must container at least one symbol')

        return password

class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'text_input',
            'placeholder': 'Username',
        })
    )
    password = forms.CharField(
        label='',
        max_length=50,
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'text_input',
            'placeholder': 'Password',
        })
    )