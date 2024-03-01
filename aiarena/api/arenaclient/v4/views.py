from rest_framework import viewsets
from aiarena.api.arenaclient.v3.views import V3ResultViewSet, V3MatchViewSet, \
    V3SetArenaClientStatusViewSet
from aiarena.api.arenaclient.v4.serializers import V4BotMatchHistorySerializer, \
    V4BotCompetitionsSerializer
from aiarena.core.permissions import IsArenaClientOrAdminUser
from aiarena.core.models import Bot


class V4MatchViewSet(V3MatchViewSet):
    pass  # No changes


class V4ResultViewSet(V3ResultViewSet):
    pass  # No changes


class V4SetArenaClientStatusViewSet(V3SetArenaClientStatusViewSet):
    pass  # No changes


class V4BotMatchHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = V4BotMatchHistorySerializer
    permission_classes = [IsArenaClientOrAdminUser]


class V4BotCompetitionHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bot.objects.all()
    serializer_class = V4BotCompetitionsSerializer
    permission_classes = [IsArenaClientOrAdminUser]
