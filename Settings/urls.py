from django.urls import path
from .views import IPA, FooterDataApi

urlpatterns = [
    path('ip/', IPA.as_view()),
    path('footer_data/', FooterDataApi.as_view())
]