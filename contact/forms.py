from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    subject = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Subject'}))
    message = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'Message'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Contact
        fields = ('subject', 'message',)
