from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'address_line1', 'address_line2',
                  'town_or_city', 'post_code', 'county',)
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders to form and remove auto-populated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address', 
            'phone_number': 'Phone Number',
            'address_line1': 'Street Address 1', 
            'address_line2': 'Street Address 2',
            'town_or_city': 'Town or City', 
            'post_code': 'Postal Code',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
