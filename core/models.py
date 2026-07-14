from django.db import models


class FounderProfile(models.Model):
    """Founder profile — editable via Django Admin without touching templates."""
    name = models.CharField(max_length=200, default="Mitanshu M. Upadhyay")
    title = models.CharField(max_length=200, default="BAMS Student & Founder, Sattvica Ayurved")
    bio = models.TextField(
        default=(
            "Mitanshu M. Upadhyay is a BAMS student and innovation enthusiast at the intersection "
            "of Artificial Intelligence, Ayurveda, and Wearable Technology. As the founder of "
            "Sattvica Ayurved, he is pioneering the fusion of ancient healing wisdom with cutting-edge "
            "technology to make personalized Ayurvedic wellness accessible to everyone."
        )
    )
    instagram_url = models.URLField(blank=True, default="https://instagram.com/")
    linkedin_url = models.URLField(blank=True, default="https://linkedin.com/in/")
    email = models.EmailField(blank=True, default="mitanshu@sattvicaayurved.com")
    photo = models.ImageField(upload_to='founder/', blank=True, null=True)

    class Meta:
        verbose_name = "Founder Profile"
        verbose_name_plural = "Founder Profile"

    def __str__(self):
        return self.name
