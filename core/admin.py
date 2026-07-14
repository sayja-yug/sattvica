from django.contrib import admin
from .models import FounderProfile


@admin.register(FounderProfile)
class FounderProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')
    fieldsets = (
        ('Personal Info', {'fields': ('name', 'title', 'bio', 'photo')}),
        ('Social Links', {'fields': ('instagram_url', 'linkedin_url', 'email')}),
    )
