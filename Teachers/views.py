from django.shortcuts import render
from .models import Teacher
from School_Management import settings
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import TeacherListSerializer

def teacher(request):
    data = Teacher.objects.filter(id=1).prefetch_related("Teacher_Education", "Teacher_Experience")
    return render(request, "teachers.html", {"value": data})

def TeacherIndex(request):

    return render(request, "teacher_index.html")

def TeacherList(request):

    t_data = Teacher.objects.all().order_by()

    return render(request, "teacher_list.html", {"td": t_data})

def TeacherDetails(request, get_id):

    tdt = Teacher.objects.filter(id=get_id).prefetch_related("Teacher_Education", "Teacher_Experience").first()
    media_url = settings.MEDIA_URL
    return render(request, "teacher_details.html", {"tdd": tdt, "media_url": media_url})

class ApiList(ListAPIView):
    permission_classes = []
    def get(self, request):
        list_data = Teacher.objects.filter()
        list_data = TeacherListSerializer(list_data, many=True).data
        return Response(list_data)