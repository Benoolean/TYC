from django.db import models
from django.contrib.auth.models import User


class RiotAccountModel(models.Model):
    riot_account_id = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)


class TournamentModel(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateField()
    status = models.IntegerField()
    tournament_id = models.CharField(max_length=200)
    tournament_code = models.CharField(max_length=200)
    