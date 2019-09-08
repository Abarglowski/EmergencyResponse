from django.contrib import admin
from django.contrib.auth.models import Permission
from . models import JobCode,Timecard,Machine
# Register your models here.
admin.site.register(JobCode)
admin.site.register(Timecard)
admin.site.register(Machine)
admin.site.register(Permission)
