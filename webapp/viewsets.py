from rest_framework import viewsets

from webapp.models import Students
from webapp.serializers import StudentsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer