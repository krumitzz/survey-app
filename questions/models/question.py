from django.db import models
#from surveys.models import Survey
from response_fields.models import (
    ChoiceField,
)

class Question(models.Model):
    #survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField('Question Text', max_length=250, help_text="e.g Level of education?")
    response_field = ChoiceField.ed_levels(ChoiceField)
    
    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'