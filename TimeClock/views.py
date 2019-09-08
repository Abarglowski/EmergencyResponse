from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from . models import JobCode,Machine,Timecard
# Create your views here.

class JobCodeView(ListView):
    model = JobCode
    template_name = 'job_code.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
