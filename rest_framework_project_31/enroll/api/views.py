from rest_framework import viewsets
from enroll.models import Student
from .serializers import StudentModelSerializer

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

