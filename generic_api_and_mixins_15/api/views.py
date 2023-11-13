from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Student
from .serializers import StudnetModelSerializer

# Create your views here.
'''
# Ex-01
class StudentList(GenericAPIView, ListModelMixin):
    
    queryset = Student.objects.all()
    serializer_class = StudnetModelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

# Ex-02
class StudentCreate(GenericAPIView, CreateModelMixin):
    
    queryset = Student.objects.all()
    serializer_class = StudnetModelSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Ex-03
class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
    
    queryset = Student.objects.all()
    serializer_class = StudnetModelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# Ex-04
class StudentUpdate(GenericAPIView, UpdateModelMixin):
    
    queryset = Student.objects.all()
    serializer_class = StudnetModelSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class studentDestroy(GenericAPIView, DestroyModelMixin):
    
    queryset = Student.objects.all()
    serializer_class = StudnetModelSerializer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

'''


# GET and POST - PK not required
class LCStudentApi(GenericAPIView, ListModelMixin, CreateModelMixin):
    
    queryset = Student.objects.all()
    serializer_class = StudnetModelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


# RETRIEVE UPDATE and DESTROY - PK required
class RUDStudentApi(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Student.objects.all()
    serializer_class = StudnetModelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)