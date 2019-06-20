from rest_framework.viewsets import ModelViewSet

from .models import Championship
from .serializers import ChampionshipSerializer


class ChampionshipViewSet(ModelViewSet):
    serializer_class = ChampionshipSerializer
    queryset = Championship.objects.all()
