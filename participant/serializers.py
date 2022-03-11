from rest_framework import serializers
from participant.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = [
            'id',
            'name',
            'age'
        ]
