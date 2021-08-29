from django import forms
from user_details.models import (
    UserDetails,
    GENDER_CHOICES
)

class UserSurveyForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(), required=True),
    age = forms.IntegerField(min_value=5, required=True)
    school_or_inst = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    department_discipline = forms.CharField(widget=forms.TextInput(), required=True)
    any_position_held = forms.CharField(widget=forms.TextInput() ,required=True)

    class Meta:
        model = UserDetails
        fields = [
            'full_name',
            'age',
            'dob',
            'school_or_inst',
            'gender',
            'department_discipline',
            'any_position_held'
        ]

    def __init__(self, *args, **kwargs):
        
        super(UserSurveyForm, self).__init__(*args, **kwargs)
        for field in (
            self.fields['full_name'],
            self.fields['age'],
            self.fields['dob'],
            self.fields['school_or_inst'],
            self.fields['gender'],
            self.fields['department_discipline'],
            self.fields['any_position_held']
            ):
            field.widget.attrs.update(
                {
                'class': 'form-control',
                }
            )
