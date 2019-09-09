from django.forms import ModelForm
from . models import JobCode, Machine

class JobCodeForm(ModelForm):
    class Meta:
        model = JobCode
        exclude = ('id',)

class MachineForm(ModelForm):
    class Meta:
        model = Machine
        exclude = ('id',)


