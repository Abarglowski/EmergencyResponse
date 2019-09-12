from django.forms import ModelForm,formset_factory
from django import forms
from . models import JobCode, Machine
from django.contrib.auth.models import User

class RegistrationMoodelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'groups',



        ]


class JobCodeForm(ModelForm):
    class Meta:
        model = JobCode
        exclude = ('id',)

class MachineForm(ModelForm):
    class Meta:
        model = Machine
        exclude = ('id','parents',)
