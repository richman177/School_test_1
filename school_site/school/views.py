from .serializers import *
from .models import *
from rest_framework import generics, viewsets, status


class HomepageListAPIView(generics.ListAPIView):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer


class SchoolListAPIView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SpecializationListAPIView(generics.ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializers


class AdminListAPIView(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class TeacherListAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TimelineListAPIView(generics.ListAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer


class GalleryListAPIView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CommunicationListAPIView(generics.ListAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer


class QualificationListAPIView(generics.ListAPIView):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer