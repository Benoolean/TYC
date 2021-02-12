from django.db import models
from django.contrib.auth.models import User

class RiotAccountModel(models.Model):
    account_id = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)