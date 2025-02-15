from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('', HomepageListAPIView.as_view(), name='homepage_list'),
    path('school/', SchoolListAPIView.as_view(), name='school_list'),
    path('specialization/', SpecializationListAPIView.as_view(), name='specialization_list'),
    path('admin/', AdminListAPIView.as_view(), name='admin_list'),
    path('teacher/', TeacherListAPIView.as_view(), name='teacher_list'),
    path('timeline/', TimelineListAPIView.as_view(), name='timeline_list'),
    path('gallery/', GalleryListAPIView.as_view(), name='gallery_list'),
    path('contact/', ContactListAPIView.as_view(), name='contact_list'),
    path('communication/', CommunicationListAPIView.as_view(), name='communication_list'),
    path('qualification/', QualificationListAPIView.as_view(), name='qualification_list'),
]