from django.contrib import admin
from .models import Skill,Question,questionBank,Assessment

admin.site.register(questionBank)
admin.site.register(Skill)
admin.site.register(Assessment)
