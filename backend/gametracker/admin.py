from django.contrib import admin
from .models import Gametracker


class GametrackerAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed")

# Register your models here.

admin.site.register(Gametracker, GametrackerAdmin)