from django.db import models


class Text(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
