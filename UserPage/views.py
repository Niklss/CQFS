from django.shortcuts import render


def role_converter(role_num):
    if role_num == 0:
        role = "Student"
    elif role_num == 1:
        role = "Student representative"
    elif role_num == 2:
        role = "Teacher assistant"
    elif role_num == 3:
        role = "Professor"
    elif role_num == 4:
        role = "Department of education"
    else:
        role = "Admin"
    return role


def user_page(request):
    user = request.user
    return render(request, 'user.html',
                  {'name': str(user.first_name) + " " + str(user.last_name), 'email': str(user.email),
                   'role': role_converter(user.role)})

