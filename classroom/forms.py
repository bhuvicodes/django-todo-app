from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    message = forms.CharField(widget = forms.Textarea)