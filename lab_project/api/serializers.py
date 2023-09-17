from rest_framework import serializers

from labs.models import Score, Test


class ScoreSerializer(serializers.ModelSerializer):
    indicator_name = serializers.SerializerMethodField()
    metric_name = serializers.SerializerMethodField()
    metric_unit = serializers.SerializerMethodField()
    is_within_normal_range = serializers.SerializerMethodField()

    class Meta:
        model = Score
        fields = (
            'id',
            'test_id',
            'score',
            'indicator_name',
            'metric_name',
            'metric_unit',
            'is_within_normal_range',
        )

    def get_indicator_name(self, obj):
        return obj.indicator_metric_id.indicator_id.name

    def get_metric_name(self, obj):
        return obj.indicator_metric_id.metric_id.name

    def get_metric_unit(self, obj):
        return obj.indicator_metric_id.metric_id.unit

    def get_is_within_normal_range(self, obj):
        return obj.min_score <= obj.score <= obj.max_score


class TestSerializer(serializers.ModelSerializer):
    duration_seconds = serializers.SerializerMethodField()
    results = ScoreSerializer(many=True, read_only=True, source='scores')

    class Meta:
        model = Test
        fields = (
            'id',
            'lab_id',
            'duration_seconds',
            'results',
        )

    def get_duration_seconds(self, obj):
        return (obj.completed_at - obj.started_at).seconds
