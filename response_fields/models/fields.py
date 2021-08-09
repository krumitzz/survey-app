from django.db import models
#from questions.models import Question


#class EmptyTextField(models.Model):
#   question_field = models.ForeignKey(Question, on_delete=models.CASCADE)
#    text_field = models.TextField(max_length=250, blank=True)

class ChoiceField(models.Model):
    LEVEL_CHOICES = [
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
]

    def ed_levels(self):
        levels = models.CharField(max_length=3, choices=self.LEVEL_CHOICES)

    def __str__(self):
        return self.title
