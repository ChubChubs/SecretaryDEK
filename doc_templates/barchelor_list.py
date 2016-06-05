__author__ = 'masterbob'
from secretary.models import Diploma, Reviewer, Chief, Commission, General, Group, HandingDay, HandingPeriod, Student


def get_students():
    for group in Group.objects.all():
        print(group.spec, group.name)
    Student.objects.all().filter()


def context():
    get_students()
    return {'groups':[
        {'group':'КН-41', 'students':
        [
            {'full_name':'Пупкін Василь Петрович', 'theme':'Типу темка1',
             'guide_name': 'Батюк А.Є.', 'guide_level':'доцент',},
            {'full_name':'Ложкін Василь Петрович', 'theme':'Типу темка2',
             'guide_name': 'Батюк А.Є.', 'guide_level':'доцент',},
            {'full_name':'Жопкін Жора Еммануїлович', 'theme':'Терморектальний криптоаналіз як універсальний інструмент стимуляції когнітивних процесів. Аналіз методів використання та характеристик струмопровідних елементів.',
             'guide_name': 'Батюк А.Є.', 'guide_level':'доцент',}
        ]
         }
    ]
    }