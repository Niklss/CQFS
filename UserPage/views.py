import requests
from django.shortcuts import render

from LogIn.models import StudentAndGroupsModel


def role_converter(role_num):
    if role_num == 5:
        role = "Admin"
    elif role_num == 1:
        role = "Student representative"
    elif role_num == 2:
        role = "Teacher assistant"
    elif role_num == 3:
        role = "Professor"
    elif role_num == 4:
        role = "Department of education"
    else:
        role = "Student"
    return role


def user_page(request):
    user = request.user
    group = StudentAndGroupsModel.objects.get(student=user.id).group
    group_str = str(group.course) + '-' + str(group)

    return render(request, 'user.html',
                  {'name': str(user.first_name) + " " + str(user.last_name), 'email': str(user.email),
                   'role': role_converter(user.role), 'group': str(group_str)})


def surveys_page(request):
    req = requests.session()
    res1 = req.request(method='GET', url="http://10.90.138.248:8000/api/surveys/surveyanswer/",
                       cookies=request.COOKIES).json()
    res2 = req.request(method='GET', url="http://10.90.138.248:8000/api/surveys/surveytemplate/",
                       cookies=request.COOKIES).json()
    return render(request, 'user_surveys.html',
                  {'response': {'surveys_answer': res1['objects'], 'surveys_template': res2['objects']}})
