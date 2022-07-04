from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Newsletter(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='newsletter_author',
        null=True,
        blank=True,

    )
    newsletter_email = models.EmailField(max_length=255)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылка'

    def __str__(self):
        return self.newsletter_email
