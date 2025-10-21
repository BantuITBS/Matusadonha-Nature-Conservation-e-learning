from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('lecturer/', views.dashboard_lecturer, name='dashboard_lecturer'),
    path('manager/', views.dashboard_manager, name='dashboard_manager'),
    path('student/', views.dashboard_student, name='dashboard_student'),
]
