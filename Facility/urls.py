from django.urls import path
from .views import facility, FacilitylistApi, facility_details, FacilityDetailsApi

urlpatterns = [
    path('', facility),
    path('details/<str:id>/', facility_details),
    path('api_list/', FacilitylistApi.as_view()),
    path('api_details/<str:id>/', FacilityDetailsApi.as_view()),
]
