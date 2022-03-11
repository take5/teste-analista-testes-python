from rest_framework.viewsets import ModelViewSet
from participant.models import Participant
from participant.serializers import ParticipantSerializer


class ParticipantView(ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
