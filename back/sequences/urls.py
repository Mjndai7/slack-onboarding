from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('sequences', views.SequenceViewSet, 'sequences')

urlpatterns = [
    path('', include(router.urls)),
    path('external_messages', views.SaveExternalMessage.as_view()),
    path('sequence/admin_task', views.SaveAdminTask.as_view())
]