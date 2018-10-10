from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Studnet(CommonInfo):
    home_group = models.CharField(max_length=5)
