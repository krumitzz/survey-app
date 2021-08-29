from django.db import models
from django.conf import settings

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('R', 'Rather Not Say')
)

class UserDetails(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE # delete user details if the user is deleted
                              )
    
    full_name = models.CharField('Full Name', max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    dob = models.DateField('Date Of Birth', blank=True, null=True)
    school_or_inst = models.CharField('School or Institution',max_length=250, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_CHOICES[2], blank=True)

    department_discipline = models.CharField('Department/Discipline', max_length=250, blank=True)
    any_position_held = models.CharField('Any Position Held', max_length=250, blank=True)
    
    
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'User Detail'
        verbose_name_plural = 'User Details'