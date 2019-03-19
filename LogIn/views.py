from django.shortcuts import render
from .models import DBHelper


def login(request):
    return render(request, 'login.html')


def sign_in(request):
    db = DBHelper()
    user = db.is_in_system(request.content_params["login"], request.content_params["password"])
    if user is not False:
        return render(request, 'user.html')
    else:
        return False


#
# def contact(request):
#     return render(request, 'personal/basic.html', {'content':['There is my email:', 'leonor13092000@mail.ru']})
