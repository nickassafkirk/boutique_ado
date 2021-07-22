from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto generated
        labels and set autofocus on first field
        """

        # We use placeholders to overide default labels for form inputs
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, state or Locality',
        }

        # set autofocus on full name field
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'  # puts a star on the placeholder if it's required
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder  # applies placholder from varable above to each forms placeholder attr
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'  # adds a css class
            self.fields[field].label = False  # removes the forms input label
