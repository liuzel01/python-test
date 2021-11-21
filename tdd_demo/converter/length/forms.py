from django import forms

class LengthConverterForm(forms.Form):
    MEASUREMENTS = (
        ('centimetre', '厘米'),
        ('metre', '米'),
        ('mile', '英里')
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    input_value = forms.DecimalField(decimal_places=3)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_value = forms.DecimalField(decimal_places=3, required=False)
