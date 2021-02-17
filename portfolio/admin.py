from django.contrib import admin
from .models import Project
# Register your models here.
#this line of code is necessary to see this page on your admin screen
admin.site.register(Project)
