from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    duration_display = serializers.CharField(source='duration', read_only=True)

    class Meta:
        model = Game
        fields = ['id', 'board', 'turn', 'winner', 'is_finished', 'created_at', 'finished_at', 'duration_display']
        read_only_fields = ['board', 'turn', 'winner', 'is_finished', 'created_at', 'finished_at']