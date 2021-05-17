from webbrowser import register

from django.contrib.auth.models import Permission
from django.contrib import admin
admin.site.register(Permission)
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','email']
    list_per_page = 15
    list_filter = ['username','first_name', 'last_name']