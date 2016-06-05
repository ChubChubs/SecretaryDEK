from django.contrib import admin
from .models import Diploma, Reviewer, Student, HandingDay, HandingPeriod,StudentsRestriction
from  .models import General, Group, Chief, Commission

"""
So these are admin models for django's default admin site.
Looks nice. Useful as an umbrella in the rain.
"""

class DiplomaAdmin(admin.ModelAdmin):
    model = Diploma
    list_display = ['theme', 'get_name', ]

    def get_name(self, obj):
        return obj.student.user.last_name + ' ' + obj.student.user.first_name
    get_name.admin_order_field  = 'student.user.last_name'  #Allows column order sorting
    get_name.short_description = 'Author Name'  #Renames column head
admin.site.register(Diploma, DiplomaAdmin)


class ReviewerAdmin(admin.ModelAdmin):
    model = Reviewer
    list_display = ['get_name', ]

    def get_name(self, obj):
        return obj.user.last_name + ' ' + obj.user.first_name
    get_name.admin_order_field  = 'user.last_name'  #Allows column order sorting
    get_name.short_description = 'Reviewer\'s Full Name'  #Renames column head
admin.site.register(Reviewer, ReviewerAdmin)


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['get_name','group']
    def get_name(self, obj):
        return obj.user.last_name + ' ' + obj.user.first_name
    get_name.admin_order_field  = 'get_name'  #Allows column order sorting
    get_name.short_description = 'Student\'s Full Name'  #Renames column head
admin.site.register(Student, StudentAdmin)

class HandWeekAdmin(admin.ModelAdmin):
    model = HandingPeriod
    list_display = ['start','end']
admin.site.register(HandingPeriod)

class HandingDayAdmin(admin.ModelAdmin):
    model = HandingDay
    list_display = ['date','start_time', 'end_time']
admin.site.register(HandingDay, HandingDayAdmin)

class StudentsRestrictionAdmin(admin.ModelAdmin):
    model = StudentsRestriction
    list_display = ['chief' , 'handingperiod', 'numberofstudents']
admin.site.register(StudentsRestriction, StudentsRestrictionAdmin)
# Register your models here.


class GeneralAdmin(admin.ModelAdmin):
    model = General
    list_display = ['get_name', ]

    def get_name(self, obj):
        return obj.user.last_name + ' ' + obj.user.first_name
    get_name.admin_order_field  = 'user.last_name'  #Allows column order sorting
    get_name.short_description = 'Користувач'  #Renames column head
admin.site.register(General, GeneralAdmin)

class GroupAdmin(admin.ModelAdmin):
    model = Group
    list_display = ['name', ]
admin.site.register(Group, GroupAdmin)


class ChiefAdmin(admin.ModelAdmin):
    model = Chief
    list_display = ['get_name', ]

    def get_name(self, obj):
        return obj.user.last_name + ' ' + obj.user.first_name + ' ' + obj.user.general.mname
    get_name.admin_order_field  = 'user.last_name'  #Allows column order sorting
    get_name.short_description = 'Керівник дипломних робіт'  #Renames column head
admin.site.register(Chief, ChiefAdmin)