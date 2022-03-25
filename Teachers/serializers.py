from rest_framework import serializers
from .models import Teacher

class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["full_name", "email", "phone"]

class TeachrListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"