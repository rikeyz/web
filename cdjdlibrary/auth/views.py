from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from cdjdlibrary.auth.forms import SingUpForm, LoginForm

from django.utils.translation import ugettext_lazy as _


def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'auth/signup.html', {'form': form})
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        return render(request, 'auth/signup.html', {'form': SingUpForm()})


def loginform(request):
    if request.user.is_authenticated():
        return redirect("/")

    return render(request, 'auth/login.html', {'form': LoginForm()})


def loginlib(request):

    if not request.method == 'POST':
        return render(request, '404.html', {'message': _('Unsupported method GET')})
    else:
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'auth/login.html', {'form': form})
        else:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is None:
                return redirect("/login.html")

            login(request, user)
            return redirect("/")


def logoutlib(request):
    logout(request=request)
    return redirect("/login.html")
