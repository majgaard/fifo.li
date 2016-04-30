from django.contrib import admin

# Register your models here.

from .models import Queue

# Register your models here.

@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    pass