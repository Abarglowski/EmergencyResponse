from django.urls import path, re_path
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from . views import EditJobCode,EditMachine,EditTimecard,JobCodeView,MachineView,TimecardView,JobCodeDelete,MachineDelete,JobCodeAdd,MachineAdd
from . models import JobCode,Machine,Timecard
from django.views.generic.edit import DeleteView

app_name='TimeClock'
urlpatterns = [
    path('jobcode/',JobCodeView.as_view(),name='Jobcode'),
    path('machine/',MachineView.as_view(),name='Machine'),
    path('timecard/',TimecardView.as_view(),name='Timecard'),
    path('edit/jobcode/<int:pk>',EditJobCode.as_view(),name='jobCodeEdit'),
    path('edit/machine/<int:pk>',EditMachine.as_view(),name='machineEdit'),
    path('edit/timecard/<int:pk>',EditTimecard.as_view(),name='timecardEdit'),
    path('delete/jobcode/<int:pk>',JobCodeDelete.as_view(),name='jobCodeDelete'),
    path('delete/machine/<int:pk>',MachineDelete.as_view(),name='machineDelete'),
    path('delete/timecard/<int:pk>',DeleteView.as_view(),name='timecardDelete'),
    path('add/jobcode/', JobCodeAdd.as_view(),name='jobCodeAdd'),
    path('add/machine/', MachineAdd.as_view(),name='machineAdd')

]