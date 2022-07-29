from django.db import models
from django.utils.translation import gettext_lazy as _

class Name(models.Model):

#    class GenderOptions(models.TextChoices):
#        MALE = 'M', _('Male')
#        FEMALE = 'F', _('Female')

    text = models.CharField(max_length = 255)
    prob_f = models.FloatField()
    prob_m = models.FloatField()
#    gender = models.CharField(
#        max_length = 1,
#        choices = GenderOptions.choices
#    )
    gender = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(
        auto_now_add = True, 
        blank = True,
        null = True)

    def __str__(self):
        return self.text 