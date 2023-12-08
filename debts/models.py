from django.db import models
from django.contrib.auth.models import User


class Debts(models.Model):
    bomdod = models.IntegerField()
    peshin = models.IntegerField()
    asr = models.IntegerField()
    shom = models.IntegerField()
    xufton = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
