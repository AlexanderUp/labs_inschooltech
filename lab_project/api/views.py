from django.db.models import OuterRef, Prefetch, Subquery
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.filters import TestFilter
from api.serializers import TestSerializer
from indicators.models import Reference
from labs.models import Score, Test


class TestViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TestSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TestFilter

    def get_queryset(self):
        scores_queryset = (
            Score.objects.select_related(
                'test_id',
                'indicator_metric_id',
            )
            .filter(is_active=True)
            .annotate(
                min_score=Subquery(
                    Reference.objects.filter(
                        is_active=True,
                        indicator_metric_id=OuterRef('indicator_metric_id'),
                    ).values('min_score'),
                ),
                max_score=Subquery(
                    Reference.objects.filter(
                        is_active=True,
                        indicator_metric_id=OuterRef('indicator_metric_id'),
                    ).values('max_score'),
                ),
            )
        )
        prefetched_scores = Prefetch('scores', queryset=scores_queryset)
        return Test.objects.filter(is_active=True).prefetch_related(
            prefetched_scores,
            'scores__indicator_metric_id__indicator_id',
            'scores__indicator_metric_id__metric_id',
        )
