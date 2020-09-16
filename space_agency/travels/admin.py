from django.contrib import admin
from .models import Travel

# Register your models here.
@admin.register(Travel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'destination','arrival_time','departure_time', 'image')