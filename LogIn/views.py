from LogIn.models import Sys_User
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.views import View


class Login(View):

    def post(self, request, *args, **kwargs):
        context = dict()
        logout(request)

        email = request.POST['email']
        password = request.POST['password']
        try:
            next_page = request.POST['next']
            if next_page == '':
                next_page = '/'
        except BaseException as e:
            next_page = None

        try:
            Sys_User_inst = Sys_User.objects.get(email=email)
        except BaseException as e:
            context['errors'] = 'Wrong e-mail or password'
            context['email'] = email
            return render(request, 'login.html', context)

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            if next_page is not None:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect('/user/')

        return render(request, 'login.html', context)

    def get(self, request, *args, **kwargs):
        context = dict()
        return render(request, 'login.html', context)
