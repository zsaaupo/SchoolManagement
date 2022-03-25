from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import FooterDataSerializers
from .models import FooterData

class IPA(ListAPIView):
    permission_classes = []

    def get(self, request):
        print(request.META)
        return Response("ok")

class FooterDataApi(ListAPIView):
    permission_classes = []

    def get(self, request):
        footer_data = FooterData.objects.filter().last()
        footer_data = FooterDataSerializers(footer_data).data
        return Response(footer_data)