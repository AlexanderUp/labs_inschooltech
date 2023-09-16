from django.contrib import admin

from labs.models import Lab, Score, Test


class LabAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created_at', 'updated_at', 'is_active')
    empty_value_display = '--empty--'


class TestAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'lab_id',
        'created_at',
        'updated_at',
        'is_active',
        'started_at',
        'completed_at',
        'comment',
    )
    empty_value_display = '--empty--'
    list_select_related = ('lab_id',)


class ScoreAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'test_id',
        'score',
        'indicator_metric_id',
        'created_at',
        'updated_at',
        'is_active',
    )
    empty_value_display = '--empty--'
    list_select_related = (
        'test_id',
        'indicator_metric_id',
        'indicator_metric_id__indicator_id',
        'indicator_metric_id__metric_id',
    )


admin.site.register(Lab, LabAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Score, ScoreAdmin)
