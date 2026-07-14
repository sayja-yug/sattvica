from django.db import models


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]


class DemoSubmission(models.Model):
    """
    Stores each interactive demo run. Viewable in Django Admin during SSIP presentation
    to demonstrate real backend functionality.
    """
    # User inputs
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    # Generated dummy dosha values (0-100)
    vata_score = models.IntegerField()
    pitta_score = models.IntegerField()
    kapha_score = models.IntegerField()

    # Generated dummy wellness metrics (0-100)
    stress_score = models.IntegerField()
    sleep_score = models.IntegerField()
    energy_score = models.IntegerField()
    wellness_score = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Demo Submission"
        verbose_name_plural = "Demo Submissions"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.gender}, {self.age}) — {self.created_at.strftime('%d %b %Y %H:%M')}"

    @property
    def dominant_dosha(self):
        scores = {'Vata': self.vata_score, 'Pitta': self.pitta_score, 'Kapha': self.kapha_score}
        return max(scores, key=scores.get)
