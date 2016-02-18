from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# For UserType we using builtin model User, that contain authorization and authentication

class Reviewer(models.Model):
    """
    Reviewer ORM. Holds typical name, surname, mname and a ID. For now.
    """
    id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True, auto_created=True)
    name = models.CharField(null=False, max_length=100, verbose_name="Ім'я")
    surname = models.CharField(null=False, max_length=100, verbose_name="Прізвище")
    mname = models.CharField(null=False, max_length=100, verbose_name="По-батькові")
    passseries = models.CharField(null=True, max_length=5, verbose_name="Серія паспорта")
    passnum = models.IntegerField(null=True, verbose_name="Номер паспорта")
    idnum = models.CharField(max_length=13, null=True, verbose_name="Ідентифікаційний код")
    passplace = models.CharField(max_length=50, null=True, verbose_name="Ким виданий")
    passdate = models.DateField(null=True, verbose_name="Коли виданий")
    graduate = models.CharField(null=True, max_length=250, verbose_name="Освіта")
    edugrade = models.CharField(null=True, max_length=10, verbose_name="Вчене звання")
    workplace = models.CharField(null=True, max_length=250, verbose_name="Місце роботи")
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
    id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True, auto_created=True)
    bdate = models.DateField(verbose_name="Дата народження")
    user = models.ForeignKey(User)
    entry2uni = models.DateField(verbose_name="Дата вступу в універ")
    registered = models.BooleanField(verbose_name="Валідний?")
    lector = models.BooleanField(verbose_name="Лектор?")
    student = models.BooleanField(verbose_name="Штюдент?")


class Diploma(models.Model):
    """
    Diplomas ORM. Contains many fields. Such as:
    Theme, year, group, review date, guide mark,
    number of pages in diploma, number of slides in the presentation
    Diploma Mark, Graduation Date(datehanding)
    Boolean Fields are type (is it a red diploma or NO) and fellowship
    Foreign Keys are Reviewer and Guide
    """
    id = models.IntegerField(verbose_name='Id',primary_key=True, unique=True, db_index=True, auto_created=True)
    theme = models.TextField(max_length=512, verbose_name="Тема")
    theme_eng = models.TextField(max_length=512, verbose_name="Тема англійською")
    year = models.IntegerField(verbose_name="Рік")
    group = models.CharField(verbose_name='Група', max_length=30)
    reviewer = models.ForeignKey(Reviewer, related_name="Рецензент", blank=True, null=True, verbose_name="Рецензент",
                                 db_constraint=False)
    datereview = models.DateField(verbose_name='Дата рецензації')
    guide = models.ForeignKey(Reviewer, blank=True, null=True, related_name="Керівник", verbose_name="Керівник",
                              db_constraint=False)
    profile = models.ForeignKey(UserProfile, blank=True, null=True, verbose_name="Профіль шановного юзверя")
    guidemark = models.IntegerField(verbose_name='Оцінка керівника')
    pageswork = models.IntegerField(verbose_name='Клькість сторінок в записці')
    pagespresentation = models.IntegerField(verbose_name='Кількість слайдів у презентації')
    datehanding = models.DateField(verbose_name="Дата захисту")
    type = models.BooleanField(verbose_name='Диплом-то червоний?')
    fellowship = models.BooleanField(verbose_name='Рекомендований в аспірантуру?')
    mark = models.IntegerField(verbose_name='Оцінка')
    special_circumstances = models.BooleanField(verbose_name="Спец обставини. Достроковий захист і проч.")

class HandWeek(models.Model):
    id = models.IntegerField(verbose_name='Id',primary_key=True, unique=True, db_index=True, auto_created=True)
    season = models.BooleanField(verbose_name='Зима?')
    start = models.DateField(verbose_name="Початок захистів")
    finish = models.DateField(verbose_name="Кінець захистів")

