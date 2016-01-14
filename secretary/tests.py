from django.test import TestCase
from .models import *
from datetime import datetime
from django.shortcuts import render
# Create your tests here.

def diploma_add_data():
    """
    Test data in DB.
    :return:
    """
    new_d = Diploma(theme = u'Типу тема',
    theme_eng = 'Some shit',
    group = 'KN-41',
    year = '2015',
    datehanding = datetime.now(),
    datereview = datetime.now(),
    guidemark = 5,
    pageswork = 100,
    pagespresentation = 10,
    type = False,
    fellowship = False,
    mark = 5,)
    new_d.save()

def guide_add_data(request):
    """
    Test data in DB.
    :return:
    """
    new_g = Guide(name = 'Вася', mname = 'Питрович', surname = 'Пупкін')
    new_g.save()
    return render(request, 'base.html')

def ref_add_data(request):
    new_g = Reviewer(name = 'Семен', mname = 'Семенович', surname = 'Горбунков')
    new_g.save()
    return render(request, 'base.html')