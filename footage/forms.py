from django import forms

class UploadFileForm(forms.Form):
    OTHER_TAG = 'OTH'
    FOOTAGE_TAGS = [
        ('ACT', 'Action Stock'),
        ('DRN', 'Drone Stock'),
        ('LND', 'Landscapes Stock'),
        (OTHER_TAG, 'Other'),
    ]

    title = forms.CharField(
        label='',
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'text_input',
            'placeholder': 'Title',
        })
    )
    tags = forms.MultipleChoiceField(
        label='',
        choices=FOOTAGE_TAGS,
        widget=forms.CheckboxSelectMultiple(

        )
    )
    description = forms.CharField(
        label='',
        max_length=1000,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'text_input',
            'placeholder': 'Description',
        })
    )
    footage_file = forms.FileField(
        label='',
    )