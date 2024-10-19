# main/forms.py
from django import forms
from .models import *

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['name', 'email', 'phone', 'message']



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
