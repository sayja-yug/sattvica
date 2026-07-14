from django.shortcuts import render
from .models import FounderProfile


def landing(request):
    """
    Main landing page — contains all 10 sections in a single scrolling page.
    Pulls founder data from DB if a FounderProfile exists, else uses defaults.
    """
    try:
        founder = FounderProfile.objects.first()
    except Exception:
        founder = None

    tech_tags = [
        'Python', 'TensorFlow', 'Django', 'SQLite', 'REST API',
        'BLE 5.0', 'Ayurvedic NLP', 'Edge Computing', 'React Native', 'Cloud Sync',
    ]

    vision_items = [
        'Global Ayurvedic wellness platform',
        '1M+ users by 2030',
        '50+ research partnerships',
        'AYUSH-certified technology',
    ]

    demo_next_steps = [
        'Your data is processed by our AI engine',
        'Vata, Pitta & Kapha scores are calculated',
        'Personalized lifestyle & diet suggestions generated',
        'Full wellness dashboard displayed instantly',
    ]

    context = {
        'founder': founder,
        'tech_tags': tech_tags,
        'vision_items': vision_items,
        'demo_next_steps': demo_next_steps,
        'page_title': 'NADI-VERSE™ | Ancient Wisdom. Future Technology.',
        'meta_description': (
            'NADI-VERSE™ by Sattvica Ayurved — An AI-powered wearable concept for '
            'personalized Ayurvedic wellness. SSIP Proof-of-Concept 2026.'
        ),
    }
    return render(request, 'core/landing.html', context)
