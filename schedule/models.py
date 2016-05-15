from django.db import models
from secretary.models import Chief
# Create your models here.
class HandingPeriod(models.Model):
    """
    An ORM for handing weeks.
    Has a field for season, start and finis of diploma handing period
    """
    # id = models.IntegerField(verbose_name='Id',primary_key=True, unique=True, db_index=True, auto_created=True)
    start = models.DateField(verbose_name="Початок захистів", unique=True, blank=True)
    end = models.DateField(verbose_name="Кінець захистів", blank=True)

    def __str__(self):
        if self.start.month > 10:
            return 'Зима ' + str(self.start.year)
        else:
            return 'Літо ' + str(self.start.year)

class HandingDay(models.Model):
    """
    An ORM for a handing day.
    Basically, it's for assigning a handing to a particular day.
    Useful. Most of the time)
    """
    # id = models.IntegerField(verbose_name='Id',primary_key=True, unique=True, db_index=True, auto_created=True)
    week = models.ForeignKey(HandingPeriod, to_field='start', db_constraint=False)
    date = models.DateField(verbose_name="День Захисту", blank=True, unique=True)
    start_time = models.TimeField(verbose_name="Час початку захистів", blank=True)
    end_time = models.TimeField(verbose_name="Час кінця захистів", blank=True)
    def __str__(self):
        return self.date.isoformat()


class StudentsRestriction(models.Model):
    """
    Restriction for guides. If someone
    has 5 places and takes 20 students, it's something bad. Isn't it?
    """
    # id = models.IntegerField(verbose_name='Id',primary_key=True, unique=True, db_index=True, auto_created=True)
    chief = models.ForeignKey(Chief, verbose_name="Керівник дипломок", db_constraint=False)
    numberofstudents = models.IntegerField(verbose_name="Кількість студентів", blank=True)
    handingperiod = models.ForeignKey(HandingPeriod, verbose_name="Тиждень захистів", to_field='start', db_constraint=False)

    def __str__(self):
        return self.guide.surname + ' ' + self.guide.name


class Commission(models.Model):
    handingday = models.OneToOneField(HandingDay,to_field='date', primary_key=True)
    chairman = models.ForeignKey(Chief, blank=True, null=True)
    commissioner1 = models.ForeignKey(Chief, blank=True, null=True)
    commissioner2 = models.ForeignKey(Chief, blank=True, null=True)
    commissioner3 = models.ForeignKey(Chief, blank=True, null=True)
    commissioner4 = models.ForeignKey(Chief, blank=True, null=True)
    commissioner5 = models.ForeignKey(Chief, blank=True, null=True)


