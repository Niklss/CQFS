from django.shortcuts import render

def login(request):
    return render(request, '/login.html')
#
# def contact(request):
#     return render(request, 'personal/basic.html', {'content':['There is my email:', 'leonor13092000@mail.ru']})