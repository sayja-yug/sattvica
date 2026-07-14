from django import forms
from .models import DemoSubmission, GENDER_CHOICES


class DemoForm(forms.ModelForm):
    """
    Simple ModelForm for the NADI-VERSE™ interactive demo.
    Only collects user-facing inputs; scores are generated server-side.
    """
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'demo-input',
            'placeholder': 'Enter your full name',
            'id': 'id_name',
            'autocomplete': 'off',
        }),
        label='Full Name',
    )
    age = forms.IntegerField(
        min_value=1,
        max_value=120,
        widget=forms.NumberInput(attrs={
            'class': 'demo-input',
            'placeholder': 'Your age (1–120)',
            'id': 'id_age',
        }),
        label='Age',
    )
    gender = forms.ChoiceField(
        choices=[('', '— Select Gender —')] + list(GENDER_CHOICES),
        widget=forms.Select(attrs={
            'class': 'demo-input demo-select',
            'id': 'id_gender',
        }),
        label='Biological Gender',
    )

    class Meta:
        model = DemoSubmission
        fields = ['name', 'age', 'gender']
