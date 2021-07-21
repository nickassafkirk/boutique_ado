from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 
                  'street_address1', 'street_address2', 
                  'town_or_city', 'postcode', 'country', 
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto generated
        labels and set autofocus on first field
        """

        # We use placeholders to overide default labels for form inputs
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': "Full Name",
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, state or Locality',
        }

        # set autofocus on full name field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'  # puts a star on the placeholder if it's required
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder  # applies placholder from varable above to each forms placeholder attr
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'  # adds a css class
            self.fields[field].label = False  # removes the forms input label
