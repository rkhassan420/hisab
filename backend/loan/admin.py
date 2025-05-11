from django.contrib import admin
from .models import Qist

class QistInfo(admin.ModelAdmin):  
    list_display = ('sr', 'date', 'amount', 't_id', 'sender', 'receiver') 

admin.site.register(Qist, QistInfo)
