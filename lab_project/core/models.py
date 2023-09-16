import uuid

from django.db import models


class CommonModelMixin(models.Model):
    pk = models.UUIDField(
        name='id',
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        verbose_name='id',
        help_text='ID',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at',
        help_text='Created at',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='updated_at',
        help_text='Updated at',
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='is_active',
        help_text='Is active?',
    )

    class Meta:
        abstract = True
