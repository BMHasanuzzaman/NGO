from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['donor_name', 'email', 'number', 'amount']
        widgets = {
            'donor_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Donor Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }
        labels = {
            'donor_name': 'Donor Name',
            'email': 'Email',
            'number': 'Number',
            'amount': 'Amount',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True