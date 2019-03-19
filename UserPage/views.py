from django.shortcuts import render


def user_page(request):
    return render(request, 'user.html')
