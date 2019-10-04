from django import forms


class CityForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = False
        self.fields['name'].widget.attrs['placeholder'] = 'City Name'

    name = forms.CharField(max_length=225)
