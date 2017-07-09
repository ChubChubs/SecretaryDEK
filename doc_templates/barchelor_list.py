__author__ = 'masterbob'
from secretary.models import Diploma, Reviewer, Chief, Commission, General, Group, HandingDay, HandingPeriod, Student


def full_name(obj):
    return obj.user.last_name + ' ' + obj.user.first_name + ' ' + obj.general.mname

def full_name_abbreviated(obj):
    return obj.user.last_name + ' ' + obj.user.first_name[0] + '.' + General.objects.get(user=obj.user).mname[0] + '.'

def is_personal():
    return False


def get_students():
    dict = {
        'groups':[],
    }
    for group in Group.objects.all().filter(spec='бакалавр'):
        group_data = {
            'group':'',
            'students':[]
        }
        #print(group.spec, group.name)
        group_data['group'] = group.name
        for student in Student.objects.all().filter(group=group):
            student_data = {}
            print(General.objects.get(user=student.user.id))
            student_data['full_name'] = student.user.last_name + ' ' \
                                        + student.user.first_name + ' ' \
                                        + General.objects.get(user=student.user).mname
            student_data['theme'] = student.diploma.theme
            student_data['guide_name'] = full_name_abbreviated(student.diploma.chief)
            student_data['guide_level'] = student.diploma.chief.position
            print(student_data)
            group_data['students'].append(student_data)
            #student_data['theme'] = student.diploma.theme
        dict['groups'].append(group_data)
    print(dict)
    return dict




def context():
    return get_students()
'''
        {'groups':[
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
'''