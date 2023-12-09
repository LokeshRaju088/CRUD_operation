# forms.py

from django import forms
from .models import Candidatedirectory, Maritalstatus, Persona


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidatedirectory
        fields = ['first_name', 'last_name', 'email', 'persona', 'status']

        marital_status = forms.ModelChoiceField(queryset=Maritalstatus.objects.all())

    widgets = {
        'persona': forms.Select(attrs={'class': 'form-control'}),
        'marital_status': forms.Select(attrs={'class': 'form-control'}),
        'status': forms.Select(attrs={'class': 'form-control'}),
    }

    # Use the actual model fields for choices
    MARITAL_STATUS_CHOICES = [('married', 'Married'), ('single', 'Single')]
    STATUS_CHOICES = [(1, 'Available for Meeting'),
                      (2, 'Not Available for Meeting')]  # Replace with your actual choices

    marital_status = forms.ChoiceField(choices=[('', 'Select Marital Status')] + list(MARITAL_STATUS_CHOICES))
    status = forms.ChoiceField(choices=[('', 'Select Status')] + list(STATUS_CHOICES))


class CandidateCreateForm(CandidateForm):
    class Meta(CandidateForm.Meta):
        pass  # No additional fields needed for creating


class CandidateUpdateForm(CandidateForm):
    class Meta(CandidateForm.Meta):
        pass  # No additional fields needed for updating