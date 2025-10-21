# courses/views.py
from rest_framework import viewsets, permissions
from .models import Course, Module
from .serializers import CourseSerializer, ModuleSerializer

from django.shortcuts import render

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

# Home page
def home(request):
    return render(request, 'home.html')  # Your homepage at templates/home.html

# Portal page (after sign-in)
def portal(request):
    return render(request, 'portal/portal_home.html')  # The main portal

# Course pages
def community_engagement(request):
    return render(request, 'portal/courses/community_engagement.html')

def leadership_skills(request):
    return render(request, 'portal/courses/leadership_skills.html')

def conflict_resolution(request):
    return render(request, 'portal/courses/conflict_resolution.html')

def digital_skills(request):
    return render(request, 'portal/courses/digital_skills.html')

def leadership_styles(request):
    return render(request, 'portal/courses/leadership_styles.html')

def supervision_delegation(request):
    return render(request, 'portal/courses/supervision_delegation.html')

def portal_home(request):
    return render(request, 'portal/portal_home.html')
