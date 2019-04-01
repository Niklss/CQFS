from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication
from .models import SurveyTemplateModel
from .models import SurveyAnswerModel
from tastypie.authentication import Authentication


class SillyAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        if 0 < request.user.role < 6:
            return True

        return False

    # Optional but recommended
    def get_identifier(self, request):
        return request.user.username




class SurveyTemplateResource(ModelResource):
    class Meta:
        queryset = SurveyTemplateModel.objects.all()
        authentication = SillyAuthentication()
        resource_name = 'surveytemplate'


class SurveyAnswerResource(ModelResource):
    class Meta:
        queryset = SurveyAnswerModel.objects.all()
        authentication = SessionAuthentication()
        resource_name = 'surveyanswer'
