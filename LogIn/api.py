from tastypie.resources import ModelResource
from .models import SurveyTemplateModel
from .models import SurveyAnswerModel

class SurveyTemplateResource(ModelResource):
    class Meta:
        queryset = SurveyTemplateModel.objects.all()
        resource_name = 'surveytemplate'

class SurveyAnswerResource(ModelResource):
    class Meta:
        queryset = SurveyAnswerModel.objects.all()
        resource_name = 'surveyanswer'

