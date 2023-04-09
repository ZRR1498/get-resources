from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('date', )
    list_filter = ('date', )
    search_fields = ('date', )
