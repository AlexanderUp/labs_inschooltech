from django.conf import settings
from django.db.models import OuterRef, Prefetch, Subquery
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.filters import TestFilter
from api.serializers import TestSerializer
from indicators.models import Reference
from labs.models import Score, Test


@method_decorator(
    cache_page(settings.API_RESPONSE_CACHE_DURATION_SECONDS),
    name='dispatch',
)
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
