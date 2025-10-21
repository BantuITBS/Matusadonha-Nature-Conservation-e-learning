from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from users import views as user_views
from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet, ModuleViewSet

# API router
router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('modules', ModuleViewSet)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Homepage
    path('', lambda request: render(request, 'home.html'), name='home'),

    # Auth views
    path('login/', user_views.login_view, name='login'),
    path('signup/', user_views.signup_view, name='signup'),

    # API routes
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),

    # Courses (portal/courses handled inside courses/urls.py)
    path('', include('courses.urls')),

    # Users
    path('users/', include('users.urls')),
]
