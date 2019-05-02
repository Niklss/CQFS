from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource

from .models import SurveyAnswerModel
from .models import SurveyTemplateModel


class SurveyTemplateResource(ModelResource):
    class Meta:
        queryset = SurveyTemplateModel.objects.all()
        authentication = SessionAuthentication()
        allowed_methods = ['get', 'post', 'put', 'patch', 'update']
        # excludes =
        resource_name = 'surveytemplate'

    def authorized_read_list(self, object_list, bundle):
        user = bundle.request.user
        queryset = SurveyTemplateModel.objects.filter(creator_id=user.id)
        return queryset

    def authorized_create_list(self, object_list, bundle):
        user = bundle.request.user
        if user.role > 0:
            answer = bundle.data
            template = SurveyTemplateModel.objects.create_survey(survey_name=answer.survey_name,
                                                                 creator_id=answer.creator_id,
                                                                 json=answer.json)
            # if not answer.group:
            #     groups = GroupsModel.objects.get(answer.course)


            return 200
        return 'Permission denied'


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

    def authorized_create_list(self, object_list, bundle):
        user = bundle.request.user
        answer = bundle.data
        SurveyTemplateModel.objects.add_survey_response(survey_id=answer.survey_id, responder_id=user.id,
                                                        json=answer.json)
        return 200
