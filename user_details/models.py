from django.db import models
from django.conf import settings

GENDER_CHOICE = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('R', 'Rather Not Say')
)

class UserDetails(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE # delete user details if the user is deleted
                              )
    
    full_name = models.CharField('Full Name', max_length=100)
    age = models.IntegerField(blank=True)
    dob = models.DateField('Date Of Birth')
    school = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default=GENDER_CHOICE[2])

    department_discipline = models.CharField('Department/Discipline', max_length=250)
    any_position_held = models.CharField('Any Position Held', max_length=250, blank=True)
    
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'User Detail'
        verbose_name_plural = 'User Details'