from LogIn.models import Sys_User
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.views import View

class Register(View):

    def post(self, request, *args, **kwargs):
        context = dict()
        logout(request)

        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        try:
            next_page = request.POST['next']
            if next_page == '':
                next_page = '/'
        except BaseException as e:
            next_page = None

        try:
            Sys_User_inst = Sys_User.objects.get(email=email)
            context['errors'] = 'This email already used'
            context['email'] = email
            return render(request, 'login.html', context)
        except BaseException as e:
            pass

        user = Sys_User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, username=username)

        if user is not None:
            login(request, user)
            if next_page is not None:
                return HttpResponseRedirect(next_page)
            else:
                return HttpResponseRedirect('/user/')

        return render(request, 'register.html', context)

    def get(self, request, *args, **kwargs):
        context = dict()
        return render(request, 'register.html', context)