from django.db import models
from django.contrib.auth.models import User
from schedule.models import HandingDay, HandingPeriod
# Create your models here.

# For UserType we using builtin model User, that contain authorization and authentication
class Group(models.Model):
    """
    Dummy group purposed mostly for dropdowns
    """
    id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True,
                             auto_created=True, blank=True)
    name = models.CharField(verbose_name="Група",max_length=40)
    barchelor = "бакалавр"
    specialist = "спеціаліст"
    phd = "магістр"
    maigster = phd
    choices = (
        (barchelor, "Бакалавр"),
        (specialist, "Спеціаліст"),
        (phd, "Магістр")
    )
    spec = models.CharField(verbose_name="напрямок (Бакалавр, Спеціаліст чи Магістр)",max_length=40, choices=choices,
                            default="Бакалавр")


class Reviewer(models.Model):
    """
    Reviewer ORM. Holds typical name, surname, mname and a ID. For now.
    """
    id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True, auto_created=True)
    user = models.OneToOneField(User, primary_key=True)
    children = models.IntegerField(null=True, verbose_name='Діти, шт.', blank=True)
    education = models.CharField(null=True, max_length=250, verbose_name="Освіта",blank=True)
    special_education = models.CharField(null=True, max_length=40, verbose_name="Спеціальна освіта",blank=True)
    academic_status = models.CharField(null=True, max_length=10, verbose_name="Вчене звання",blank=True)
    degree = models.CharField(null=True, max_length=10, verbose_name="Науковий ступінь",blank=True)
    position = models.CharField(null=True, max_length=250, verbose_name="Посада",blank=True)
    workplace = models.CharField(null=True, max_length=250, verbose_name="Місце роботи",blank=True)
    def __str__(self):
        return self.user.last_name + ' ' + self.user.first_name


class Chief(models.Model):
    """
    Diploma Chief ORM. Holds typical name, surname, mname and a ID. For now.
    """
    id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True,
                             auto_created=True, blank=True)
    user = models.OneToOneField(User, primary_key=True)
    education = models.CharField(null=True, max_length=250, verbose_name="Освіта",blank=True)
    special_education = models.CharField(null=True, max_length=40, verbose_name="Спеціальна освіта",blank=True)
    academic_status = models.CharField(null=True, max_length=10, verbose_name="Вчене звання",blank=True)
    degree = models.CharField(null=True, max_length=10, verbose_name="Науковий ступінь",blank=True)
    position = models.CharField(null=True, max_length=250, verbose_name="Посада",blank=True)
    def __str__(self):
        return self.user.last_name + ' ' + self.user.first_name


class General(models.Model):
    """
    User extention ORM. Foreign key - UserType.
    ID == PK
    Standard fields are in the User Model
    Date Fields - bdate (Birth) and entry2uni
    Boolean Field - registered
    """
    # id = models.IntegerField(verbose_name='Id', primary_key=True, unique=True, db_index=True, auto_created=True)
    user = models.OneToOneField(User, primary_key=True)
    bdate = models.DateField(verbose_name="Дата народження")
    mname = models.CharField(null=False, max_length=100, verbose_name="По-батькові")
    home = models.CharField(null=True, max_length=250, verbose_name="Місце проживання",blank=True)
    passseries = models.CharField(null=True, max_length=5, verbose_name="Серія паспорта",blank=True)
    passnum = models.IntegerField(null=True, verbose_name="Номер паспорта",blank=True)
    passplace = models.CharField(max_length=50, null=True, verbose_name="Ким виданий",blank=True)
    passdate = models.DateField(null=True, verbose_name="Коли виданий",blank=True)
    idnum = models.CharField(max_length=13, null=True, verbose_name="Ідентифікаційний код",blank=True)
    registered = models.BooleanField(verbose_name="Валідний?")

    def __str__(self):
        return self.user.last_name + ' ' + self.user.first_name
    def full_name(self):
        return self.user.last_name + ' ' + self.user.first_name + ' ' + self.mname
    def full_name_abbreviated(self):
        return self.user.last_name + ' ' + self.user.first_name[0] + '.' + self.mname[0] + '.'


class Student(models.Model):
    """

    """
    user = models.OneToOneField(User, primary_key=True)
    entry2uni = models.DateField(verbose_name="Дата вступу в універ")
    group = models.ForeignKey(Group)



class Diploma(models.Model):
    """
    Diplomas ORM. Contains many fields. Such as:
    Theme, year, group, review date, guide mark,
    number of pages in diploma, number of slides in the presentation
    Diploma Mark, Graduation Date(datehanding)
    Boolean Fields are type (is it a red diploma or NO) and fellowship
    Foreign Keys are Reviewer and Guide
    """
    # id = models.IntegerField(verbose_name='Id',primary_key=True, unique=True, db_index=True, auto_created=True)
    student = models.OneToOneField(Student)
    theme = models.TextField(max_length=512, verbose_name="Тема")
    theme_eng = models.TextField(max_length=512, verbose_name="Тема англійською", blank=True)
    group = models.ForeignKey(Group)
    reviewer = models.ForeignKey(Reviewer, related_name="Рецензент", blank=True, null=True, verbose_name="Рецензент",
                                 db_constraint=False)
    datereview = models.DateField(verbose_name='Дата рецензації', blank=True)
    chief = models.ForeignKey(Chief, blank=True, null=True, related_name="Керівник", verbose_name="Керівник",
                              db_constraint=False)
    chiefmark = models.IntegerField(verbose_name='Оцінка керівника', blank=True)
    numberofpages = models.IntegerField(verbose_name='Клькість сторінок в записці', blank=True)
    numberofslides = models.IntegerField(verbose_name='Кількість слайдів у презентації', blank=True)
    handingdate = models.ForeignKey(HandingDay, to_field='date', verbose_name="Дата захисту")
    type = models.BooleanField(verbose_name='Диплом-то червоний?', blank=True)
    approval = models.BooleanField(verbose_name='Диплом-то зарев’юваний?', default=False)
    fellowship = models.BooleanField(verbose_name='Рекомендований в аспірантуру?', blank=True)
    commissionmark = models.IntegerField(verbose_name='Оцінка', blank=True)
    special_circumstances = models.NullBooleanField(verbose_name="Спец обставини. Достроковий захист і проч.")
    number = models.IntegerField(verbose_name="Номер диплому в архіві",unique=True, blank=True, null=True)

    def __str__(self):
        return self.student.user.last_name + ' ' + self.student.user.first_name



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
        return self.chief.user.last_name + ' ' + self.chief.user.first_name


class Commission(models.Model):
    handingday = models.OneToOneField(HandingDay,to_field='date', primary_key=True)
    chairman = models.ForeignKey(Chief, blank=True, null=True, related_name='chairman')
    commissioner1 = models.ForeignKey(Chief, blank=True, null=True, related_name='comm1')
    commissioner2 = models.ForeignKey(Chief, blank=True, null=True, related_name='comm2')
    commissioner3 = models.ForeignKey(Chief, blank=True, null=True, related_name='comm3')
    commissioner4 = models.ForeignKey(Chief, blank=True, null=True, related_name='comm4')
    commissioner5 = models.ForeignKey(Chief, blank=True, null=True, related_name='comm5')