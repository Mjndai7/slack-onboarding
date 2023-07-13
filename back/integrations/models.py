from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from fernet_fields import EncryptedTextField
import uuid

# Create your models here.
INTEGRATION_OPTIONS = (
    (0, 'Slack'),
    (1, 'Slack Account'),
    (2, 'Google'),
    (3, 'Google Login')
)
STATUS = (
    (0, 'pending'),
    (1, 'completed'),
    (2, 'waiting on user')
)


class AccessToken(models.Model):
    integration = models.IntegerField(choices=INTEGRATION_OPTIONS)
    token = EncryptedTextField(max_length=10000, null=True, blank=True)
    refresh_token = EncryptedTextField(max_length=10000, null=True, blank=True)
    base_url = models.CharField(max_length=22300, null=True, blank=True)
    redirect_url = models.CharField(max_length=22300, null=True, blank=True)
    account_id = models.CharField(max_length=22300, null=True, blank=True)
    name = models.CharField(max_length=22300, null=True, blank=True)
    active = models.BooleanField(default=True)
    ttl = models.IntegerField(null=True, blank=True)
    expiring = models.DateTimeField(null=True, blank=True)
    one_time_auth_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Slack
    app_id = models.CharField(max_length=100, null=True)
    client_id = models.CharField(max_length=100, null=True)
    client_secret = models.CharField(max_length=100, null=True)
    signing_secret = models.CharField(max_length=100, null=True)
    verification_token = models.CharField(max_length=100, null=True)
    bot_token = EncryptedTextField(max_length=10000, null=True, blank=True)
    bot_id = models.CharField(max_length=100, null=True)


class ScheduledAccess(models.Model):
    new_hire = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    integration = models.IntegerField(choices=INTEGRATION_OPTIONS)
    status = models.IntegerField(choices=STATUS, default=0)
    email = models.EmailField(max_length=22300, null=True, blank=True)
