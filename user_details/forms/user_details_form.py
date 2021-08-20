from django import forms
from user_details.models import UserDetails

class UserDetailsForm(forms.ModelForm):
    owner = forms.CharField(hidden=True)
    class Meta:
        model = UserDetails
        fields = [
            'owner',
            'full_name',
            'age',
            'dob',
            'school_or_inst',
            'gender',
            'department_discipline',
            'any_position_held'
        ]

    def __init__(self, *args, **kwargs):
        
        super(UserDetails, self).__init__(*args, **kwargs)
        for field in self.fields:
            field.widget.attrs.update(
                {
                'class': 'form-control',
                }
                )
