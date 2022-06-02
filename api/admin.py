from django.contrib import admin
from .models import Entries

@admin.register(Entries)
class Admin_Entries(admin.ModelAdmin):
    list_display = ('id','name','price','type','desc')