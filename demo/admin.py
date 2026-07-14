from django.contrib import admin
from .models import DemoSubmission


@admin.register(DemoSubmission)
class DemoSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'age', 'gender',
        'vata_score', 'pitta_score', 'kapha_score',
        'wellness_score', 'created_at',
    )
    list_filter = ('gender', 'created_at')
    search_fields = ('name',)
    readonly_fields = (
        'vata_score', 'pitta_score', 'kapha_score',
        'stress_score', 'sleep_score', 'energy_score',
        'wellness_score', 'created_at',
    )
    fieldsets = (
        ('User Input', {'fields': ('name', 'age', 'gender')}),
        ('Dosha Analysis (Generated)', {
            'fields': ('vata_score', 'pitta_score', 'kapha_score'),
            'description': 'These are AI-generated dummy values for demo purposes.',
        }),
        ('Wellness Metrics (Generated)', {
            'fields': ('stress_score', 'sleep_score', 'energy_score', 'wellness_score'),
        }),
        ('Metadata', {'fields': ('created_at',)}),
    )
