from django.urls import path, include
from rest_framework import routers
from resources import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('resource', views.ResourceViewSet, 'resource')

urlpatterns = [
    path('', include(router.urls)),
]