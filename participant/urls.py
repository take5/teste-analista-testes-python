from django.urls import path, include
from rest_framework import routers

from participant.views import (
    ParticipantView
)

app_name = 'participant'

router = routers.DefaultRouter()
router.register(r'', ParticipantView, basename='participant')
urlpatterns = [
    path('', include(router.urls)),
]
