from django import forms
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField

class FormName(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
