from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView,TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from TimeClock.models import Timecard, Machine, JobCode

# Create your views here.

class JobCodeView(ListView):
    model = JobCode
    template_name = 'job_code.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class MachineView(ListView):
    model = Machine
    template_name = 'machine.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class TimecardView(ListView):
    model = Timecard
    template_name = 'timecard.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class EditJobCode(UpdateView):
    model = JobCode
    fields = ['jobCode','description','hourlyRate','maxHoursPerDay']
    template_name = 'job_code_edit.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(EditJobCode,self).form_valid(form)

class EditMachine(UpdateView):
    model = Machine
    fields = ['machineCode','description','hourlyRent','maxHoursPerDay']
    template_name = 'machine_edit.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(EditMachine,self).form_valid(form)

class EditTimecard(UpdateView):
    model = Timecard
    fields = ['siteCode','contractorName','totalHours','totalAmount']
    template_name = 'timecard_edit.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(EditTimecard,self).form_valid(form)

class JobCodeDelete(DeleteView):
    model = JobCode

    def get_success_url(self):
        return reverse('TimeClock:Jobcode')

class MachineDelete(DeleteView):
    model = Machine

    def get_success_url(self):
        return reverse('TimeClock:Machine')

class JobCodeAdd(CreateView):
    model = JobCode
    fields = ['jobCode','description','hourlyRate','maxHoursPerDay']
    template_name = 'job_code_add.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(JobCodeAdd,self).form_valid(form)

class MachineAdd(CreateView):
    model = Machine
    fields = ['machineCode','description','hourlyRent','maxHoursPerDay']
    template_name = 'machine_add.html'
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(MachineAdd,self).form_valid(form)

class TimecardAdd(ListView):
    model = JobCode
    context_object_name = 'timecard_form'
    template_name = 'timecard_jobcode.html'

    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        return context

class TimecardAdd2(ListView):
    model = Machine
    template_name = 'timecard_jobcode.html'
    def get_context_data(self,**kwargs):
        context= super(TimecardAdd2,self).get_context_data(**kwargs)
        context['JobCode']=JobCode.objects.all()
        return context









#class TimecardDelete(DeleteView):
#   model = Timecard

    
