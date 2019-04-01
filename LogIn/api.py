from tastypie.resources import ModelResource
from .models import SurveyTemplateModel
from .models import SurveyAnswerModel
from tastypie.authentication import Authentication


class SillyAuthenticationSurveyTemplate(Authentication):
    def is_authenticated(self, request, **kwargs):
        if 0 < request.user.role <= 5:
          return True

        return False

    # Optional but recommended
    def get_identifier(self, request):
        return request.user.username


class SillyAuthenticationSurveyAnswer(Authentication):
    def is_authenticated(self, request, **kwargs):
        if request.user.role >= 0:
          return True

        return False

    # Optional but recommended
    def get_identifier(self, request):
        return request.user.username


class SurveyTemplateResource(ModelResource):
    class Meta:
        queryset = SurveyTemplateModel.objects.all()
        resource_name = 'surveytemplate'
        authentication = SillyAuthenticationSurveyTemplate()


class SurveyAnswerResource(ModelResource):
    class Meta:
        queryset = SurveyAnswerModel.objects.all()
        resource_name = 'surveyanswer'
        authentication = SillyAuthenticationSurveyAnswer()
