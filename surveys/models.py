from django.db import models
from django.shortcuts import (
    reverse,
)

from questions.models import Question

from django.conf import settings
class Survey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField('Survey Name', max_length=255)
    questions = models.ManyToManyField(Question)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Survey'
        verbose_name_plural = 'Surveys'