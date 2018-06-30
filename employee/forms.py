from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','mail','User_name', 'password']

        label = {
            'password': 'Password'

        }

    """def clean_mail(self): 
         if self.cleaned_data['mail'].endwith('@pylgmail.com'):
             return self.cleaned_data['mail']
        else:
            raise ValidationError("mail_id is not valid")"""

    def save(self):
        password = self.cleaned_data.pop('password')
        u = super().save()
        u.set_password(password)
        u.save()
        return u
