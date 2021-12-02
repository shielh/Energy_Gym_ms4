from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Email Address'}))
    message = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'Message'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)
