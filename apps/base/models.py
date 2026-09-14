from django.db import models
from django.conf import settings


class Audit(models.Model):
    """Auditting fields that all tables should have."""

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class UserAudit(Audit):
    """User auditting fields that all user related tables should have"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    class Meta:
        abstract = True
