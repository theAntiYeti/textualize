from django.db import models


class Text(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()


class Word(models.Model):
    NEW = "NEW"
    LEARNING = "LEARNING"
    LEARNED = "LEARNED"
    progress_choices = [
        (NEW, "new"),
        (LEARNING, "learning"),
        (LEARNED, "learned"),
    ]

    word = models.CharField(max_length=20, unique=True)
    progress = models.CharField(
        max_length=8,
        choices=progress_choices
    )