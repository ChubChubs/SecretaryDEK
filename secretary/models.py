from django.db import models

# Create your models here.


'''

Diploma
Type	Name	Description
int	Id	-
string	Theme	Тема
int	Year	Рік
string	Group	Група
ReviewerId	Reviewer	Рецензент
Date	DateReview	дата рецензування
GuideId	Guide	Керівник
int	GuideMark	Оцінка керівника
int	PagesWork	К-сть сторю зап.
int	PagesPresentation	К-ть стр. презент.
Date	DateHanding	Дата захисту
bool	Type	Колір диплому
bool	Fellowship	Аспірантура
int	Mark	Оцінка

'''


class UserType(models.Model):
    """
    User type ORM. Holds only ID of a type and a verbose name of that type.
    """
    id = models.IntegerField(unique=True, db_index=True, primary_key=True)
    typename = models.CharField(max_length=50, unique=True, null=False)


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


class User(models.Model):
    """
    User ORM. Foreign key - UserType.
    ID == PK
    Standard fields name, surname, mname.
    Date Fields - bdate (Birth) and entry2uni
    Boolean Field - registered
    login and password to be enhanced. Maybe.
    """
    id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True)
    name = models.CharField(null=False, max_length=100)
    surname = models.CharField(null=False, max_length=100)
    mname = models.CharField(null=False, max_length=100)
    bdate = models.DateField()
    entry2uni = models.DateField()
    userid = models.ForeignKey(UserType)
    registered = models.BooleanField(null=False)
    login = models.CharField(max_length=30, null=False)
    password = models.CharField(null=False)


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
    year = models.IntegerField(verbose_name="year")
    group = models.CharField(verbose_name='group', max_length=30)
    reviewer = models.ForeignKey(Reviewer)
    datereview = models.DateField(verbose_name='review_date')
    guide = models.ForeignKey(Guide)
    guidemark = models.IntegerField(verbose_name='guide_mark')
    pageswork = models.IntegerField(verbose_name='pages_work')
    pagespresentation = models.IntegerField(verbose_name='presentation_pages')
    datehanding = models.DateField()
    type = models.BooleanField(verbose_name='diploma_type')
    fellowship = models.BooleanField(verbose_name='fellowship')
    mark = models.IntegerField(verbose_name='mark')
