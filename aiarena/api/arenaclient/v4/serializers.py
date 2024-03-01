from rest_framework import serializers
from aiarena.core.models import Bot, MatchParticipation, CompetitionParticipation


class V4MatchParticipationSerializer(serializers.ModelSerializer):
    map_name = serializers.SerializerMethodField()

    def get_map_name(self, obj):
        return obj.match.map.name

    started = serializers.SerializerMethodField()

    def get_started(self, obj):
        return obj.match.started

    match_id = serializers.SerializerMethodField()

    def get_match_id(self, obj):
        return obj.match.id

    class Meta:
        model = MatchParticipation
        fields = ["match_id", "map_name", "started", "result", "result_cause"]
        read_only_fields = ["match_id", "map_name", "started", "result", "result_cause"]


class V4CompetitionParticipationSerializer(serializers.ModelSerializer):

    competition_name = serializers.SerializerMethodField()

    def get_competition_name(self, obj):
        return obj.competition.name

    competition_type = serializers.SerializerMethodField()

    def get_competition_type(self, obj):
        return obj.competition.name

    competition_date_opened = serializers.SerializerMethodField()

    def get_competition_date_opened(self, obj):
        return obj.competition.date_opened

    competition_date_closed = serializers.SerializerMethodField()

    def get_competition_date_closed(self, obj):
        return obj.competition.date_closed

    competition_id = serializers.SerializerMethodField()

    def get_competition_id(self, obj):
        return obj.competition.id

    class Meta:
        model = CompetitionParticipation
        fields = ["competition_id", "competition_name", "competition_type",
                  "match_count", "win_count", "loss_count", "tie_count",
                  "crash_count", "competition_date_opened", "competition_date_closed"]


class V4BotSerializer(serializers.ModelSerializer):
    plays_race = serializers.SerializerMethodField()

    def get_plays_race(self, obj):
        return race_name(obj.plays_race.label)

    class Meta:
        model = Bot
        fields = ["id", 'plays_race', "name"]
        read_only_fields = ["id", 'plays_race', "name"]


class V4BotCompetitionsSerializer(V4BotSerializer):

    competition_history = V4CompetitionParticipationSerializer(
        many=True, read_only=True, source="competition_participations")

    class Meta:
        model = Bot
        fields = ["id", 'plays_race', "name", "competition_history"]
        read_only_fields = ["id", 'plays_race', "name", "competition_history"]


class V4BotMatchHistorySerializer(V4BotSerializer):
    match_history = V4MatchParticipationSerializer(
        many=True, read_only=True, source="matchparticipation_set")

    class Meta:
        model = Bot
        fields = ["id", 'plays_race', "name", "match_history"]
        read_only_fields = ["id", 'plays_race', "name", "match_history"]


def race_name(label):
    from aiarena.core.models.bot_race import BotRace
    race_dict = dict(BotRace.RACES)
    return race_dict[label]
