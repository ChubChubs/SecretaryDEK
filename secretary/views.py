from django.shortcuts import render
# Create your views here.
from .models import Diploma

def show_base(request):
    return render(request, 'base.html')

def show_page(request):
    # Дізнатися хто ти?(Студік чи лектор)
    ansDiploma = Diploma.objects.filter(profile__user=request.user)
    # зареквестити відповідну модель
    return render(request, 'diploma_list.html', {"tasks": ansDiploma})