from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.template.defaulttags import register
from .forms import RegisterForm

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('first_name')
            messages.success(request, 'Successful registration, try login again')
            form.save()
            return redirect('access')
    context = {"form": form}
    return render(request, 'registration.html', context)

def access(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.user.role in ('A'):
                return redirect('crud')
            return redirect(request.GET.get('next') or 'home')
        else:
            messages.error(request, 'Usuario o contraseña inválidos!', extra_tags='danger')
    return render(request, 'access.html', {})


def LOG_OUT(request):
    logout(request)
    return redirect('home')