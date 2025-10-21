from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portal/', views.portal, name='portal'),

    # Courses
    path('portal/courses/community-engagement/', views.community_engagement, name='community_engagement'),
    path('portal/courses/leadership-skills/', views.leadership_skills, name='leadership_skills'),
    path('portal/courses/conflict-resolution/', views.conflict_resolution, name='conflict_resolution'),
    path('portal/courses/digital-skills/', views.digital_skills, name='digital_skills'),
    path('portal/courses/leadership-styles/', views.leadership_styles, name='leadership_styles'),
    path('portal/courses/supervision-delegation/', views.supervision_delegation, name='supervision_delegation'),
    path('portal/', views.portal_home, name='portal_home'),
]
