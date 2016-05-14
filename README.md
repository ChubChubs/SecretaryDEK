# SecretaryDEK

So this is a readme for SecretaryDEK project.
This django app was created to automate things. And it kinda works!

### To install the dependencies
There is an automation script provided in the repo. (_CentOS/RHEL/DEbian/Ubuntu_)
just run
````bash
sudo ./autoinstall.sh
````

The suggested "proper way" to install all the requirements via pip
and to run the django from virtualenv. Heh)

So the first thing to do with your python installation - is to get a virtualenv!
(Tou might specify a version of pip and further virtualenv to run. Like pip3.4 or pip-2.7. or virtualenv-3.4)

````bash
sudo pip install virtualenv
````
Then create a virtualenv

````bash
virtualenv new_venv
source new_venv/bin/activate
````

And you're ready to install some requirements

````bash
sudo pip install -f requirements.txt
````

And this far you are able to run the app.
But we must create an admin for our DB firstly.
````bash
python3.4 manage.py createsuperuser
python3.4 manage.py runserver
````

And that's all! Your server must be up and running on http://127.0.0.1:8000/

###### Unit name: Гриць
1.  В’юшка для студіка.
    Він вводить дані про свій дипльом і забиває собі день захисту.

2.  В’юшка для рецензентів (викладачів).
    Він бачить всіх опездолів які на нього підписані. Разом з коротким описом.
    (Дата захисту, Тема (Перші 50 символів))

3.  В’юшка - список вже згенерованих документів.
    Ідея: Доки тримати в монгах, а все решта в sqlite. І через pymongo всьо діставати/відображати.

4.  В’юшка - для темплейтів.
    В ідеаі - інтерфейс через який можна закинути шаблон і агрегатор даних під нього.
###### Unit name: Бодя
1.  Рефакторнути generator

2.  Запиляти шаблончеги і агрегаторчеги для шаблончегів.

3.  Приглядати за Грицем. Виписувати піздюлі по мірі надобності. В тому числі і собі.
