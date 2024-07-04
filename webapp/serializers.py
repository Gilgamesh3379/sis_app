from rest_framework import serializers

from webapp.models import Students


class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ['id', 'first_name']