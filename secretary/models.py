from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# For UserType we using builtin model User, that contain authorization and authentication

class Reviewer(models.Model):
    """
    Reviewer ORM. Holds typical name, surname, mname and a ID. For now.
    """
    #id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True, auto_created=True)
    name = models.CharField(null=False, max_length=100, verbose_name="Ім'я")
    surname = models.CharField(null=False, max_length=100, verbose_name="Прізвище",unique=True)
    mname = models.CharField(null=False, max_length=100, verbose_name="По-батькові")
    passseries = models.CharField(null=True, max_length=5, verbose_name="Серія паспорта")
    passnum = models.IntegerField(null=True, verbose_name="Номер паспорта")
    idnum = models.CharField(max_length=13, null=True, verbose_name="Ідентифікаційний код")
    passplace = models.CharField(max_length=50, null=True, verbose_name="Ким виданий")
    passdate = models.DateField(null=True, verbose_name="Коли виданий",blank=True)
    bdate = models.DateField(null=True, verbose_name="Рік народження",blank=True)
    children = models.IntegerField(null=True, verbose_name='Діти, шт.', blank=True)
    graduate = models.CharField(null=True, max_length=250, verbose_name="Освіта")
    extra_graduate = models.CharField(null=True, max_length=10, verbose_name="Спеціальна освіта")
    edugrade = models.CharField(null=True, max_length=10, verbose_name="Вчене звання")
    level = models.CharField(null=True, max_length=10, verbose_name="Науковий ступінь")
    position = models.CharField(null=True, max_length=250, verbose_name="Посада")
    workplace = models.CharField(null=True, max_length=250, verbose_name="Місце роботи")
    home = models.CharField(null=True, max_length=250, verbose_name="Місце проживання")
    redundant_dude = models.NullBooleanField(verbose_name="Не з політехніки?")
    def __unicode__(self):
        return self.surname + ' ' + self.name
    def __str__(self):
        return self.surname + ' ' + self.name
'''
class Guide(models.Model):
    """
    Guideman ORM. Holds typical name, surname, mname and a ID. For now.
    """
    id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True)
    name = models.CharField(null=False, max_length=100)
    surname = models.CharField(null=False, max_length=100)
    mname = models.CharField(null=False, max_length=100)

# TODO: Create application "Account", that contain all information about user, login, logout, session.

'''
class UserProfile(models.Model):
    """
    User ORM. Foreign key - UserType.
    ID == PK
    Standard fields are in the User Model
    Date Fields - bdate (Birth) and entry2uni
    Boolean Field - registered
    login and password to be enhanced. Maybe.
    """
    # id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True, auto_created=True)
    bdate = models.DateField(verbose_name="Дата народження")
    user = models.ForeignKey(User)
    mname = models.CharField(null=False, max_length=100, verbose_name="По-батькові")
    entry2uni = models.DateField(verbose_name="Дата вступу в універ")
    registered = models.BooleanField(verbose_name="Валідний?")
    lector = models.BooleanField(verbose_name="Лектор?")
    student = models.BooleanField(verbose_name="Штюдент?")
    def __unicode__(self):
        return self.user.last_name + ' ' + self.user.first_name
    def __str__(self):
        return self.user.last_name + ' ' + self.user.first_name
    def full_name(self):
        return self.user.last_name + ' ' + self.user.first_name + ' ' + self.mname


class Diploma(models.Model):
    """
    Diplomas ORM. Contains many fields. Such as:
    Theme, year, group, review date, guide mark,
    number of pages in diploma, number of slides in the presentation
    Diploma Mark, Graduation Date(datehanding)
    Boolean Fields are type (is it a red diploma or NO) and fellowship
    Foreign Keys are Reviewer and Guide
    """
    #id = models.IntegerField(verbose_name='Id',primary_key=True, unique=True, db_index=True, auto_created=True)
    theme = models.TextField(max_length=512, verbose_name="Тема")
    theme_eng = models.TextField(max_length=512, verbose_name="Тема англійською", blank=True)
    year = models.IntegerField(verbose_name="Рік")
    group = models.CharField(verbose_name='Група', max_length=30)
    reviewer = models.ForeignKey(Reviewer, related_name="Рецензент", blank=True, null=True, verbose_name="Рецензент",
                                 db_constraint=False, to_field='surname')
    datereview = models.DateField(verbose_name='Дата рецензації', blank=True)
    guide = models.ForeignKey(Reviewer, blank=True, null=True, related_name="Керівник", verbose_name="Керівник",
                              db_constraint=False, to_field='surname')
    profile = models.ForeignKey(UserProfile, blank=True, null=True, verbose_name="Профіль шановного юзверя")
    guidemark = models.IntegerField(verbose_name='Оцінка керівника', blank=True)
    pageswork = models.IntegerField(verbose_name='Клькість сторінок в записці', blank=True)
    pagespresentation = models.IntegerField(verbose_name='Кількість слайдів у презентації', blank=True)
    datehanding = models.DateField(verbose_name="Дата захисту", blank=True)
    type = models.BooleanField(verbose_name='Диплом-то червоний?', blank=True)
    fellowship = models.BooleanField(verbose_name='Рекомендований в аспірантуру?', blank=True)
    mark = models.IntegerField(verbose_name='Оцінка', blank=True)
    special_circumstances = models.NullBooleanField(verbose_name="Спец обставини. Достроковий захист і проч.")
    def __unicode__(self):
        return self.profile.user.last_name + ' ' + self.profile.user.last_name
    def __str__(self):
        return self.profile.user.last_name + ' ' + self.profile.user.last_name


class HandWeek(models.Model):
    """
    An ORM for handing weeks.
    Has a field for season, start and finis of diploma handing period
    """
    #id = models.IntegerField(verbose_name='Id',primary_key=True, unique=True, db_index=True, auto_created=True)
    season = models.BooleanField(verbose_name='Зима?', blank=True)
    start = models.DateField(verbose_name="Початок захистів", unique=True, blank=True)
    finish = models.DateField(verbose_name="Кінець захистів", blank=True)
    def __unicode__(self):
        return self.start.isoformat()
    def __str__(self):
        return self.start.isoformat()

class HandingDay(models.Model):
    """
    An ORM for a handing day.
    Basically, it's for assigning a handing to a particular day.
    Useful. Most of the time)
    """
    #id = models.IntegerField(verbose_name='Id',primary_key=True, unique=True, db_index=True, auto_created=True)
    week = models.ForeignKey(HandWeek, to_field='start', db_constraint=False)
    date = models.DateField(verbose_name="День Захисту", blank=True)
    start_time = models.TimeField(verbose_name="Час початку захистів", blank=True)
    end_time = models.TimeField(verbose_name="Час кінця захистів", blank=True)
    def __unicode__(self):
        return self.date.isoformat()
    def __str__(self):
        return self.date.isoformat()


class StudentsRestriction(models.Model):
    """
    Restriction for guides. If someone
    has 5 places and takes 20 students, it's something bad. Isn't it?
    """
    #id = models.IntegerField(verbose_name='Id',primary_key=True, unique=True, db_index=True, auto_created=True)
    guide = models.ForeignKey(Reviewer, verbose_name="Керівник дипломок", db_constraint=False)
    numberofstudents = models.IntegerField(verbose_name="Кількість студентів", blank=True)
    handweek = models.ForeignKey(HandWeek, verbose_name="Тиждень захистів", to_field='start', db_constraint=False)
    def __unicode__(self):
        return self.guide.surname + ' ' + self.guide.name
    def __str__(self):
        return self.guide.surname + ' ' + self.guide.name