from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# For UserType we using builtin model User, that contain authorization and authentication

class Reviewer(models.Model):
    """
    Reviewer ORM. Holds typical name, surname, mname and a ID. For now.
    """
    id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True)
    name = models.CharField(null=False, max_length=100)
    surname = models.CharField(null=False, max_length=100)
    mname = models.CharField(null=False, max_length=100)


class Guide(models.Model):
    """
    Guideman ORM. Holds typical name, surname, mname and a ID. For now.
    """
    id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True)
    name = models.CharField(null=False, max_length=100)
    surname = models.CharField(null=False, max_length=100)
    mname = models.CharField(null=False, max_length=100)

# TODO: Create application "Account", that contain all information about user, login, logout, session.


class UserProfile(models.Model):
    """
    User ORM. Foreign key - UserType.
    ID == PK
    Standard fields are in the User Model
    Date Fields - bdate (Birth) and entry2uni
    Boolean Field - registered
    login and password to be enhanced. Maybe.
    """
    id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True)
    bdate = models.DateField()
    user = models.ForeignKey(User)
    entry2uni = models.DateField()
    registered = models.BooleanField(null=False)


class Diploma(models.Model):
    """
    Diplomas ORM. Contains many fields. Such as:
    Theme, year, group, review date, guide mark,
    number of pages in diploma, number of slides in the presentation
    Diploma Mark, Graduation Date(datehanding)
    Boolean Fields are type (is it a red diploma or NO) and fellowship
    Foreign Keys are Reviewer and Guide
    """
    id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True)
    theme = models.TextField(max_length=512)
    theme_eng = models.TextField(max_length=512)
    year = models.IntegerField(verbose_name="year")
    group = models.CharField(verbose_name='group', max_length=30)
    reviewer = models.ForeignKey(Reviewer, blank=True, null=True)
    datereview = models.DateField(verbose_name='review_date')
    guide = models.ForeignKey(Guide, blank=True, null=True)
    profile = models.ForeignKey(UserProfile, blank=True, null=True)
    guidemark = models.IntegerField(verbose_name='guide_mark')
    pageswork = models.IntegerField(verbose_name='pages_work')
    pagespresentation = models.IntegerField(verbose_name='presentation_pages')
    datehanding = models.DateField()
    type = models.BooleanField(verbose_name='diploma_type')
    fellowship = models.BooleanField(verbose_name='fellowship')
    mark = models.IntegerField(verbose_name='mark')
