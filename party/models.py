import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class Party(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    party_date = models.DateTimeField()
    party_time = models.TimeField()
    invitation = models.TextField()
    venue = models.CharField(max_length=255)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_parties')

    class Meta:
        verbose_name_plural = "parties"

    def __str__(self):
        return f"{self.venue}, {self.party_date}"


class Gift(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    gift = models.CharField(max_length=255)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    link = models.URLField(max_length=200, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.gift)


class Guest(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    attending = models.BooleanField(default=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='guests')

    def __str__(self):
        return str(self.name)
