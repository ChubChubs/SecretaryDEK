from django.contrib import admin
from .models import Diploma, Reviewer, UserProfile, HandingDay, HandWeek,StudentsRestriction

admin.site.register(Diploma)
admin.site.register(Reviewer)
admin.site.register(UserProfile)
admin.site.register(HandWeek)
admin.site.register(HandingDay)
admin.site.register(StudentsRestriction)
# Register your models here.
