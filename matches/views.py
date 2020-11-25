from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import AllowAny
from .models import Matches, IPLSeason
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import json
from django.forms.models import model_to_dict
from teams.models import Team

@api_view(['GET', 'POST'])
def index(request):
    return Response({"data": "This is the body field..."}, status=200)



class season_list(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        try:
            data = serializers.serialize(
                "json", IPLSeason.objects.all())
            json_data = {"status": "success", "data": json.loads(data)}
            return Response(json_data)
        except:
            return Response({"status": "failed"}, status=404)



class matches_list(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        try:
            data = serializers.serialize(
                "json", Matches.objects.filter(year=IPLSeason.objects.get(pk=2020)))
            json_data = {"status": "success", "data": json.loads(data)}
            return Response(json_data)
        except:
            return Response({"status": "failed"}, status=404)



class matches_list_season(APIView):
    permission_classes = (AllowAny, )
    def get(self, request, pk):
        try:
            data = serializers.serialize(
                "json", Matches.objects.filter(year=IPLSeason.objects.get(pk=pk)))
            json_data = {"status": "success", "data": json.loads(data)}
            return Response(json_data)
        except:
            return Response({"status": "failed"}, status=404)



class add_match(APIView):
    permission_classes = (AllowAny, )
    def post(self, request):
        try:
            # print(request.data)
            data = request.data
            # print(data["year"])
            ipl = IPLSeason.objects.get(pk=data["year"])
            team1 = Team.objects.filter(team_name=data["team_one"], year=IPLSeason.objects.get(pk=data["year"]))[0]
            team2 = Team.objects.filter(team_name=data["team_two"], year=IPLSeason.objects.get(pk=data["year"]))[0]
            toss = Team.objects.filter(team_name=data["toss"], year=IPLSeason.objects.get(pk=data["year"]))[0]
            match_won = Team.objects.filter(team_name=data["match_won"], year=IPLSeason.objects.get(pk=data["year"]))[0]

            print(data["elected"].upper()[0])
            match = Matches(year=ipl, team_one=team1, team_two=team2, team_one_txt=data["team_one"], team_two_txt=data["team_two"], toss_txt=data["toss"], match_won_txt=data["match_won"], toss=toss, elected=data["elected"].upper()[0], first_inning_score=data["first_inning_score"], second_inning_score=data["second_inning_score"], first_inning_over=data["first_inning_over"], second_inning_over=data["second_inning_over"], match_won=match_won )
            match.save()

            Team.objects.filter(team_name=data["team_one"], year=IPLSeason.objects.get(pk=data["year"])).update(total_matches=data["new_total_matches_1"], wins=data["new_wins_1"], losses=data["new_losses_1"], points=data["new_points_1"], nrr=data["new_nrr_1"])
            Team.objects.filter(team_name=data["team_two"], year=IPLSeason.objects.get(pk=data["year"])).update(total_matches=data["new_total_matches_2"], wins=data["new_wins_2"], losses=data["new_losses_2"], points=data["new_points_2"], nrr=data["new_nrr_2"])

            return Response({"status": "success"}, status=201)
        except AttributeError:
            return Response({"status": "failed", "err_message": "Please enter the valid attribute credential"}, status=403)
        except ValueError:
            return Response({"status": "failed", "err_message": "Please enter the valid credential"}, status=403)
