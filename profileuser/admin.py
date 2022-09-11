from django.contrib import admin
from .models import Profile,MasterEdu,WorkExperience,Notes

# Register your models here.

admin.site.register(Profile)
admin.site.register(MasterEdu)
admin.site.register(WorkExperience)
admin.site.register(Notes)
