from django.conf import settings
from django.db import models

from core.models import CommonModelMixin


class Indicator(CommonModelMixin):
    name = models.TextField(
        verbose_name='name',
        help_text="Indicator's name",
    )
    description = models.TextField(
        verbose_name='description',
        help_text='Indicator description',
    )

    class Meta:
        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicators'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Indicator <{self.name}>'


class Metric(CommonModelMixin):
    name = models.TextField(
        verbose_name='name',
        help_text="Indicator's name",
    )
    description = models.TextField(
        verbose_name='description',
        help_text='Indicator description',
    )
    unit = models.TextField(
        verbose_name='unit',
        help_text="Metric's unit",
    )

    class Meta:
        verbose_name = 'Metric'
        verbose_name_plural = 'Metrics'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Metric <{self.name}>'


class IndicatorMetric(CommonModelMixin):
    indicator_id = models.ForeignKey(
        Indicator,
        on_delete=models.CASCADE,
        related_name='indicator_metrics',
        verbose_name='indicator_id',
        help_text='Indicator id',
    )
    metric_id = models.ForeignKey(
        Metric,
        on_delete=models.CASCADE,
        related_name='indicator_metrics',
        verbose_name='metric_id',
        help_text='Metric id',
    )

    class Meta:
        verbose_name = 'Indicator Metric'
        verbose_name_plural = 'Indicator Metrics'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Indicator Metric <{self.indicator_id} - {self.metric_id}>'


class Reference(CommonModelMixin):
    indicator_metric_id = models.ForeignKey(
        IndicatorMetric,
        on_delete=models.CASCADE,
        related_name='references',
        verbose_name='indicator_metric_id',
        help_text='IndicatorMetric id',
    )
    min_score = models.DecimalField(
        max_digits=settings.TEST_SCORE_PRECISION_MAX_DIGITS,
        decimal_places=settings.TEST_SCORE_PRECISION_DECIMAL_PLACES,
        verbose_name='min_score',
        help_text='Min score',
    )
    max_score = models.DecimalField(
        max_digits=settings.TEST_SCORE_PRECISION_MAX_DIGITS,
        decimal_places=settings.TEST_SCORE_PRECISION_DECIMAL_PLACES,
        verbose_name='max_score',
        help_text='Max score',
    )

    class Meta:
        verbose_name = 'Reference'
        verbose_name_plural = 'References'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Reference <{self.indicator_metric_id}>'
