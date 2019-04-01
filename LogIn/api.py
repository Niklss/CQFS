from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication
from .models import SurveyTemplateModel
from .models import SurveyAnswerModel


class SurveyTemplateResource(ModelResource):
    class Meta:
        queryset = SurveyTemplateModel.objects.all()
        authentication = SessionAuthentication()
        resource_name = 'surveytemplate'

class SurveyAnswerResource(ModelResource):
    class Meta:
        queryset = SurveyAnswerModel.objects.all()
        queryset = SurveyTemplateModel.objects.create_survey()
        authentication = SessionAuthentication()
        resource_name = 'surveyanswer'

