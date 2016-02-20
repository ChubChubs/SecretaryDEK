from django.contrib import admin
from .models import Diploma, Reviewer, UserProfile, HandingDay, HandWeek,StudentsRestriction

"""
So these are admin models for django's default admin site.
Looks nice. Useful as an umbrella in the rain.
"""

class DiplomaAdmin(admin.ModelAdmin):
    model = Diploma
    list_display = ['theme', 'get_name', ]

    def get_name(self, obj):
        return obj.profile.user.last_name + obj.profile.user.first_name
    get_name.admin_order_field  = 'profile.user.last_name'  #Allows column order sorting
    get_name.short_description = 'Author Name'  #Renames column head
admin.site.register(Diploma, DiplomaAdmin)


class ReviewerAdmin(admin.ModelAdmin):
    model = Reviewer
    list_display = ['get_name', ]

    def get_name(self, obj):
        return obj.surname + ' ' + obj.name
    get_name.admin_order_field  = 'surname'  #Allows column order sorting
    get_name.short_description = 'Reviewer\'s Full Name'  #Renames column head
admin.site.register(Reviewer, ReviewerAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ['get_name','registered', 'student', 'lector']
    def get_name(self, obj):
        return obj.user.last_name + ' ' + obj.user.first_name
    get_name.admin_order_field  = 'get_name'  #Allows column order sorting
    get_name.short_description = 'Student\'s Full Name'  #Renames column head
admin.site.register(UserProfile, UserProfileAdmin)

class HandWeekAdmin(admin.ModelAdmin):
    model = HandWeek
    list_display = ['start','finish', 'season']
admin.site.register(HandWeek)

class HandingDayAdmin(admin.ModelAdmin):
    model = HandingDay
    list_display = ['date','start_time', 'end_time']
admin.site.register(HandingDay, HandingDayAdmin)

class StudentsRestrictionAdmin(admin.ModelAdmin):
    model = StudentsRestriction
    list_display = ['guide' , 'handweek', 'numberofstudents']
admin.site.register(StudentsRestriction, StudentsRestrictionAdmin)
# Register your models here.
