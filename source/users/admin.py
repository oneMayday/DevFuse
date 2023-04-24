from django.contrib import admin

from users.models import Profile, Technologie, Specialization


admin.site.register(Profile)
admin.site.register(Technologie)
admin.site.register(Specialization)
