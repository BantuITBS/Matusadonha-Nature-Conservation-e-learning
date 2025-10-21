from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('portal_home')  # redirect to portal
    else:
        form = UserCreationForm()
    return render(request, 'home.html', {'signup_form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('portal_home')  # redirect to portal
    else:
        form = AuthenticationForm()
    return render(request, 'home.html', {'login_form': form})

def dashboard_lecturer(request):
    return render(request, 'portal/dashboard_lecturer.html')

def dashboard_manager(request):
    return render(request, 'portal/dashboard_manager.html')

def dashboard_student(request):
    return render(request, 'portal/dashboard_student.html')
