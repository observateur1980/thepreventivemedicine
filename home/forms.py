from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=120, widget=forms.TextInput(attrs={'id':'contact_input','class':'contact_input', 'placeholder':'Your Name', 'required':'required'}))
    phone = forms.CharField(label='', max_length=12, widget=forms.TextInput(attrs={'id':'contact_phone','class':'contact_input', 'placeholder':'Your Phone', 'required':'required'}))
    email = forms.EmailField(label='', max_length=120, widget=forms.EmailInput(attrs={'id':'contact_email','class':'contact_input', 'placeholder':'Your E-mail', 'required':'required'}))
    subject = forms.CharField(label='', max_length=120, widget=forms.TextInput(attrs={'id':'contact_subject','class':'contact_input', 'placeholder':'Subject', 'required':'required'}))
    message = forms.CharField(label='', max_length=120, widget=forms.Textarea(attrs={'id':'contact_textarea','class':'contact_input contact_textarea', 'placeholder':'Message', 'required':'required'}))

   