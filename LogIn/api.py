from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication
from .models import SurveyTemplateModel
from .models import SurveyAnswerModel


class SurveyTemplateResource(ModelResource):
    class Meta:
        queryset = SurveyTemplateModel.objects.all()
        authentication = SessionAuthentication()
        allowed_methods = ['get', 'post', 'put', 'patch', 'update']
        # excludes =
        resource_name = 'surveytemplate'

    def authorized_read_list(self, object_list, bundle):
        user = bundle.request.user
        queryset = SurveyTemplateModel.objects.filter(responder_id=user.id)
        return queryset


class SurveyAnswerResource(ModelResource):
    class Meta:
        queryset = SurveyAnswerModel.objects.all()
        authentication = SessionAuthentication()
        allowed_methods = ['get', 'post']
        # excludes =
        resource_name = 'surveyanswer'

    def authorized_read_list(self, object_list, bundle):
        user = bundle.request.user
        queryset = SurveyAnswerModel.objects.filter(responder_id=user.id)
        return queryset

    # Need to think about it

    # def authorized_create_list(self, object_list, bundle):
    #     user = bundle.request.user
    #     answer = bundle.data
    #     SurveyTemplateModel.objects.create()
    #     return 200
