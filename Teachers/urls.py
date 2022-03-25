from django.contrib import admin
from django.urls import path, include
from .views import TeacherIndex, TeacherList, TeacherDetails, teacher, ApiList

urlpatterns = [
    path('', TeacherIndex),
    path('list/', TeacherList),
    path('details/<str:get_id>/', TeacherDetails),
    path('old/', teacher),
    path('api_list/', ApiList.as_view())  # api
]