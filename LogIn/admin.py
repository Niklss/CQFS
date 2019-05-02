from django.contrib import admin

from LogIn.models import Sys_User, SurveyTemplateModel, SurveyAnswerModel, GroupsModel, StudentAndGroupsModel, \
    CourseModel

admin.site.register(Sys_User)
admin.site.register(CourseModel)
admin.site.register(GroupsModel)
admin.site.register(StudentAndGroupsModel)
admin.site.register(SurveyTemplateModel)
admin.site.register(SurveyAnswerModel)
