from django.db import models


class Shortner(models.Model):
    long_url = models.CharField(max_length=255)
    short_url = models.CharField(max_length=20)
