from django.db import models
from django.contrib import admin


class iot(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    information=models.JSONField(default=dict(temperature=0,humidity=0,moisture=0));

    def __str__(self):
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")

