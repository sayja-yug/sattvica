"""
Utility functions for the NADI-VERSE™ demo app.

The dummy report generation logic is isolated here so it can be swapped out
for a real ML model in future without changing views.py.
"""
import random


# Lifestyle & diet suggestions mapped by dominant dosha
DOSHA_SUGGESTIONS = {
    'Vata': {
        'lifestyle': [
            'Maintain a consistent daily routine (dinacharya)',
            'Practice grounding yoga poses: Tadasana, Virabhadrasana',
            'Avoid excessive travel and screen time before bed',
            'Warm oil self-massage (Abhyanga) with sesame oil daily',
        ],
        'diet': [
            'Favor warm, oily, and nourishing foods',
            'Include ghee, sesame seeds, almonds, and warm milk',
            'Eat at regular intervals; avoid fasting',
            'Reduce raw vegetables, cold drinks, and caffeine',
        ],
        'routine': [
            'Wake up by 6:30 AM; practice Pranayama for 10 minutes',
            'Meditate for 15 minutes each morning',
            'Early dinner (before 7 PM); light, cooked foods',
            'Sleep by 10 PM to balance Vata energy',
        ],
    },
    'Pitta': {
        'lifestyle': [
            'Avoid excessive heat, direct sun, and overworking',
            'Practice cooling yoga: Sitali Pranayama, moon salutations',
            'Take breaks during work to prevent burnout',
            'Spend time in nature near water for calming effect',
        ],
        'diet': [
            'Favor cooling, sweet, and bitter foods',
            'Include coconut water, cucumber, mint, and leafy greens',
            'Avoid spicy, fried, and fermented foods',
            'Limit alcohol, red meat, and excessive salt',
        ],
        'routine': [
            'Wake by 6:00 AM; practice Sheetali breathing',
            'Exercise during cooler parts of the day (morning/evening)',
            'Avoid skipping meals; maintain meal discipline',
            'Wind down with 10 min of gratitude journaling before sleep',
        ],
    },
    'Kapha': {
        'lifestyle': [
            'Engage in vigorous daily exercise for at least 45 minutes',
            'Avoid daytime napping; keep mentally stimulated',
            'Practice dynamic yoga: Surya Namaskar, Kapalbhati',
            'Vary your daily routine to prevent stagnation',
        ],
        'diet': [
            'Favor light, dry, and warming foods',
            'Include ginger, turmeric, black pepper, and honey',
            'Reduce dairy, sweets, and heavy/oily foods',
            'Eat lighter meals; intermittent fasting is beneficial',
        ],
        'routine': [
            'Wake up before 6 AM; early rising energizes Kapha types',
            'Dry brushing (Garshana) before shower to stimulate circulation',
            'Avoid heavy meals in the evening',
            'Engage in stimulating social activities to lift energy',
        ],
    },
}


def generate_dummy_report(name: str, age: int, gender: str) -> dict:
    """
    Generate a deterministic dummy Ayurvedic wellness report.

    Uses a seed derived from name + age + gender for reproducibility —
    the same person always gets the same results during the demo.

    Returns a dict with all score fields and suggestions.
    """
    # Deterministic seed
    seed_str = f"{name.lower().strip()}{age}{gender.lower()}"
    seed = sum(ord(c) for c in seed_str) * age
    rng = random.Random(seed)

    # Generate raw dosha weights (must sum to 100)
    v = rng.randint(20, 60)
    p = rng.randint(20, 60)
    k = rng.randint(20, 60)
    total = v + p + k
    vata = round(v / total * 100)
    pitta = round(p / total * 100)
    kapha = 100 - vata - pitta  # ensure exact 100

    # Wellness metrics influenced by age and dosha
    stress = rng.randint(25, 75)
    sleep = rng.randint(45, 90)
    energy = rng.randint(40, 95)
    wellness = round((sleep + energy + (100 - stress)) / 3)

    # Determine dominant dosha
    dosha_scores = {'Vata': vata, 'Pitta': pitta, 'Kapha': kapha}
    dominant = max(dosha_scores, key=dosha_scores.get)
    suggestions = DOSHA_SUGGESTIONS[dominant]

    return {
        'vata_score': vata,
        'pitta_score': pitta,
        'kapha_score': kapha,
        'stress_score': stress,
        'sleep_score': sleep,
        'energy_score': energy,
        'wellness_score': wellness,
        'dominant_dosha': dominant,
        'suggestions': suggestions,
    }
