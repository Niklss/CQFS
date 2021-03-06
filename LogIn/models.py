from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password, username=None, first_name=None, last_name=None, role=0):
        user = self.model(email=email, password=password,
                          username=username, first_name=first_name, last_name=last_name, role=role)
        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if Sys_User.objects.all().count() > 0:
            username = 'user_{}'.format(Sys_User.objects.latest('id').id + 1)
        else:
            username = 'user_1'

        user = self.create_user(email=email, password=password, username=username)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Sys_User(AbstractUser):
    email = models.EmailField(_('email'), max_length=40, unique=True)
    first_name = models.CharField(_('first_name'), max_length=40, null=True)
    last_name = models.CharField(_('last_name'), max_length=40, null=True)
    role = models.IntegerField(_('role'), null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomAccountManager()

    class Meta:
        verbose_name = _('User')

    verbose_name_plural = _('Users')

    def __str__(self):
        return self.email


class CourseManager(models.Manager):
    def create_course(self, course_name):
        course = self.model(course_name=course_name)
        return course


class CourseModel(models.Model):
    course_name = models.CharField(max_length=40, unique=True)
    objects = CourseManager()

    class Meta:
        verbose_name = _('Course')

    verbose_name_plural = _('Courses')

    def __str__(self):
        return self.course_name


class GroupsManager(models.Manager):
    def create_group(self, group_name, course_id):
        group = self.model(group_name=group_name, course_id=course_id)
        return group


class GroupsModel(models.Model):
    group_name = models.CharField(max_length=40, unique=True)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    objects = GroupsManager()

    class Meta:
        verbose_name = _('Group')

    verbose_name_plural = _('Groups')

    def __str__(self):
        return self.group_name


class StudentAndGroupsManager(models.Manager):
    def add_to_group(self, group_id, student_id):
        group = self.model(group=group_id, student=student_id)
        return group


class StudentAndGroupsModel(models.Model):
    group = models.ForeignKey(GroupsModel, on_delete=models.CASCADE)
    student = models.ForeignKey(Sys_User, on_delete=models.CASCADE)
    objects = StudentAndGroupsManager()


class SurveyTemplateManager(models.Manager):
    def create_survey(self, creator_id, groups_id, json):
        survey_template = self.model(creator_id=creator_id, groups_id=groups_id, json=json)
        return survey_template

    def modify_survey(self, id, creator_id, groups_id, json):
        survey_template = self.model.objects.get(id=id)
        survey_template.creator_id = creator_id
        survey_template.groups_id = groups_id
        survey_template.json = json
        survey_template.save(using=self._db)
        return survey_template

    def delete_survey(self, id):
        survey_template = self.model.objects.get(id=id).delete()
        return survey_template


class SurveyTemplateModel(models.Model):
    survey_name = models.CharField(max_length=255)
    creator_id = models.ForeignKey(Sys_User, on_delete=models.CASCADE)
    groups_id = models.CharField(max_length=255)
    json = JSONField()
    objects = SurveyTemplateManager()

    class Meta:
        verbose_name = _('SurveyTemplate')

    verbose_name_plural = _('SurveyTemplates')

    def __int__(self):
        return self.id


class SurveyAnswerManager(models.Manager):
    def add_survey_response(self, survey_id, responder_id, json):
        survey = self.model(survey_id=survey_id, responder_id=responder_id, json=json)
        return survey


class SurveyAnswerModel(models.Model):
    survey_name = models.CharField(max_length=255)
    survey_id = models.ForeignKey(SurveyTemplateModel, on_delete=models.CASCADE)
    responder_id = models.ForeignKey(Sys_User, on_delete=models.CASCADE)
    json = JSONField()
    objects = SurveyAnswerManager()

    class Meta:
        verbose_name = _('SurveyAnswer')

    verbose_name_plural = _('SurveyAnswers')

    def __int__(self):
        return self.survey_id


class SurveysAndGroupsManager(models.Manager):
    def add_to_surveys_table(self, group_id, survey_template):
        entity = self.model(group=group_id, survey_template=survey_template)
        return entity


class SurveysAndGroupsModel(models.Model):
    group = models.ForeignKey(GroupsModel, on_delete=models.CASCADE)
    survey_template = models.ForeignKey(SurveyTemplateModel, on_delete=models.CASCADE)
    objects = SurveysAndGroupsManager()
