from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','text']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control m-2'})