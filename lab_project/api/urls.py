from django.urls import include, path
from rest_framework.routers import DefaultRouter

# isort: split
from api.views import TestViewSet

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register('tests', TestViewSet, basename='tests')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
