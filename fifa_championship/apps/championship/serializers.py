from rest_framework import serializers

from .models import Championship


class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = ("id", "name", "start_date", "end_date", "created_at")
        ready_only_fields = ("id", "created_at")
