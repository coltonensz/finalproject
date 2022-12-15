from django.contrib import admin
from .models import Job
from .models import Contact


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Job)
admin.site.register(Contact)

