from django.contrib import admin
from .models import*
# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ['name', 'password']



admin.site.register(userdata, AdminUser)