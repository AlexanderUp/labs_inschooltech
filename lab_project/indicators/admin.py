from django.contrib import admin

from indicators.models import Indicator, IndicatorMetric, Metric, Reference


class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'created_at', 'updated_at', 'is_active')
    empty_value_display = '--empty--'


class MetricAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'description',
        'unit',
        'created_at',
        'updated_at',
        'is_active',
    )
    empty_value_display = '--empty--'


class IndicatorMetricAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'indicator_id',
        'metric_id',
        'created_at',
        'updated_at',
        'is_active',
    )
    empty_value_display = '--empty--'
    list_select_related = ('indicator_id', 'metric_id')


class ReferenceAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'indicator_metric_id',
        'min_score',
        'max_score',
        'created_at',
        'updated_at',
        'is_active',
    )
    empty_value_display = '--empty--'
    list_select_related = (
        'indicator_metric_id',
        'indicator_metric_id__indicator_id',
        'indicator_metric_id__metric_id',
    )


admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Metric, MetricAdmin)
admin.site.register(IndicatorMetric, IndicatorMetricAdmin)
admin.site.register(Reference, ReferenceAdmin)
