from django.db import models
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
    period = models.ForeignKey(HandingPeriod, to_field='start', db_constraint=False)
    date = models.DateField(verbose_name="День Захисту", blank=True, unique=True)
    start_time = models.TimeField(verbose_name="Час початку захистів", blank=True)
    end_time = models.TimeField(verbose_name="Час кінця захистів", blank=True)
    def __str__(self):
        return self.date.isoformat()





