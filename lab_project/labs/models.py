from django.conf import settings
from django.db import models

from core.models import CommonModelMixin
from indicators.models import IndicatorMetric


class Lab(CommonModelMixin):
    name = models.TextField(
        verbose_name='name',
        help_text="Lab's name",
        unique=True,
    )

    class Meta:
        verbose_name = 'Lab'
        verbose_name_plural = 'Labs'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Lab <{self.name}>'


class Test(CommonModelMixin):
    lab_id = models.ForeignKey(
        Lab,
        on_delete=models.CASCADE,
        related_name='tests',
        verbose_name='lab_id',
        help_text="Lab's id",
    )
    started_at = models.DateTimeField(
        verbose_name='started_at',
        help_text='Test started at',
    )
    completed_at = models.DateTimeField(
        verbose_name='completed_at',
        help_text='Test completed at',
    )
    comment = models.TextField(
        verbose_name='comment',
        help_text="Test's comment",
    )

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Test <{self.pk}>'


class Score(CommonModelMixin):
    test_id = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='scores',
        verbose_name='test_id',
        help_text='Test id',
    )
    score = models.DecimalField(
        max_digits=settings.TEST_SCORE_PRECISION_MAX_DIGITS,
        decimal_places=settings.TEST_SCORE_PRECISION_DECIMAL_PLACES,
        verbose_name='score',
        help_text='Score',
    )
    indicator_metric_id = models.ForeignKey(
        IndicatorMetric,
        on_delete=models.CASCADE,
        related_name='scores',
        verbose_name='indicator_metric_id',
        help_text='IndicatorMetric id',
    )

    class Meta:
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'
        ordering = ('-created_at',)

    def __str__(self):
        return f'Score <{self.score} - {self.indicator_metric_id}>'
