# http://127.0.0.1:8000/admin/
from django.contrib import admin
from .models import Record
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'city', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'city')
    list_filter = ('city', 'state', 'created_at')
