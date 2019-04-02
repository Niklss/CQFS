from django.contrib import admin
from LogIn.models import Sys_User, SurveyTemplateModel, SurveyAnswerModel

admin.site.register(Sys_User)
admin.site.register(SurveyTemplateModel)
admin.site.register(SurveyAnswerModel)