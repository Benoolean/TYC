from django.contrib import admin

from .models import TournamentModel, RiotAccountModel

# Register your models here.
admin.site.register(TournamentModel)
admin.site.register(RiotAccountModel)