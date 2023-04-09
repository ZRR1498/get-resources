from django.contrib import admin
from .models import Data


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('date', 'value', )
    list_filter = ('date', )
    search_fields = ('date', )
