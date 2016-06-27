from django.db import models


class ServerTestKV(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.key
