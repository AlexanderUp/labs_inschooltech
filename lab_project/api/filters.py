from django_filters import rest_framework as filters

# isort: split
from labs.models import Test


class TestFilter(filters.FilterSet):
    lab_id = filters.UUIDFilter(field_name='lab_id')

    class Meta:
        model = Test
        fields = ('lab_id',)
