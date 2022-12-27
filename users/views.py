from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.core.exceptions import ValidationError


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                raise ValidationError('Пользователь %s уже существует' % username)
            elif User.objects.filter(email=email).exists():
                raise ValidationError('Пользователь %s уже существует' % email)
            else:
                user = User.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password1
                )
                user.set_password(password1)
                user.save()
                user = auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                print('created sucessfully')
                return redirect('/')
        else:
            raise ValidationError('Неправильный пароль')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('Wrongas;odlkas;dlkapkd')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')