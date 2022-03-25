from django.urls import path
from .views import student, student_index, ApiList, student_list, student_details, ApiDetails, student_sing_up, ApiSingUp, ApiOTPCheck, SignInAPI, student_sing_in, StudentPostAPI, student_post, StudentPostlistAPI

urlpatterns = [
    # # path('test/', test)
    path('class/<str:class_input>/', student),
    path('', student_index),
    path('list/', student_list),
    path('student_details/<str:id>/', student_details),
    path('student_sing_up/', student_sing_up),
    path('student_sing_in/', student_sing_in),
    path('student_post/', student_post),

    #API

    path('api_list', ApiList.as_view()),
    path('api_details/<str:id>/', ApiDetails.as_view()),
    path('api_student_sing_up/', ApiSingUp.as_view()),
    path('otp_check_api/', ApiOTPCheck.as_view()),
    path('api_student_sing_in/', SignInAPI.as_view()),
    path('student_post_api/', StudentPostAPI.as_view()),
    path('student_post_list_api/', StudentPostlistAPI.as_view()),
]