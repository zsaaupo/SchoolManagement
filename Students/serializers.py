from rest_framework import serializers
from .models import Student, StudentPost, ClassInfo, GuardianInfo
from django.contrib.auth.models import User

class StudentLintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "full_name", "gender", "father_name", "phone", "fee"]

class ClassInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassInfo
        fields = ["Class", "roll", "section", "admission_date"]

class GuardianInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuardianInfo
        fields = ["full_name", "phone", "NID_card", "blood_group"]

class StudentDetailsSerializer(serializers.ModelSerializer):
    Guardian_Info = GuardianInfoSerializer(many=True)
    Class_info = ClassInfoSerializer(many=True)
    class Meta:
        model = Student
        fields = ["id", "full_name", "profile_picture", "father_name", "mother_name", "gender", "religion", "birth_date", "email", "phone", "address", "blood_group", "nationality", "Guardian_Info", "Class_info"]


class StudentPostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class StudentPostSerializer(serializers.ModelSerializer):
    user = StudentPostUserSerializer(many=False)
    class Meta:
        model = StudentPost
        fields = ["id", "user", "post_picture", "post_text", "create_at", "modified_at"]
