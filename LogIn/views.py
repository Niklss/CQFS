from django.shortcuts import render
from . models import DBHelper


def login(request):
    if len(request.GET) > 0:
        db = DBHelper()
        a = request.GET["email"]
        b = request.GET["password"]
        user = db.is_in_system(a, b)
        if user is not None:
            return render(request, 'user.html')
    return render(request, 'login.html')


#
# def contact(request):
#     return render(request, 'personal/basic.html', {'content':['There is my email:', 'leonor13092000@mail.ru']})
