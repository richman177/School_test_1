from django.urls import path, include
from .views import *
from rest_framework import routers
from django.urls import path
from .views import TeacherCountView


router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('homepage/', HomepageListAPIView.as_view(), name='homepage_list'),
    path('school/', SchoolListAPIView.as_view(), name='school_list'),
    path('specialization/', SpecializationListAPIView.as_view(), name='specialization_list'),
    path('users/', AdminListAPIView.as_view(), name='admin_list'),
    path('teacher/', TeacherListAPIView.as_view(), name='teacher_list'),
    path('teachers/', TeacherAPIView.as_view(), name='teacher'),
    path('timeline/', TimelineListAPIView.as_view(), name='timeline_list'),
    path('gallery/', GalleryListAPIView.as_view(), name='gallery_list'),
    path('contact/', ContactListAPIView.as_view(), name='contact_list'),
    path('communication/', CommunicationListAPIView.as_view(), name='communication_list'),
    path('qualification/', QualificationListAPIView.as_view(), name='qualification_list'),
    path('teacher_count/', TeacherCountView.as_view(), name='teacher_count'),
]