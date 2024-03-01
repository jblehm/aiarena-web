from rest_framework.routers import DefaultRouter
from aiarena.api.arenaclient.v4.views import V4BotMatchHistoryViewSet, V4MatchViewSet, \
    V4ResultViewSet, V4SetArenaClientStatusViewSet, V4BotCompetitionHistoryViewSet

router = DefaultRouter()

router.register(r"next-match", V4MatchViewSet, basename="v4_ac_next_match")
router.register(r"submit-result", V4ResultViewSet, basename="v4_ac_submit_result")
router.register(r"set-status", V4SetArenaClientStatusViewSet, basename="v4_api_ac_set_status")
router.register(r"bot-match-history", V4BotMatchHistoryViewSet, basename="v4_api_bot_matches")
router.register(r"bot-competition-history", V4BotCompetitionHistoryViewSet,
                basename="v4_api_bot_competitions")

urlpatterns = router.urls
