from django.shortcuts import render
from .models import Facility
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import FacilityListSerializer

def facility(request):
    return render(request, 'facility_list.html')

def facility_details(request, id):
    return render(request, 'facility_details.html')

class FacilitylistApi(ListAPIView):
    permission_classes = []
    def get(self, request):
        facility_data = Facility.objects.filter()
        facility_data = FacilityListSerializer(facility_data, many=True).data
        return Response(facility_data)

class FacilityDetailsApi(ListAPIView):
    permission_classes = []
    def get(self, request, id):
        facility_details_data = Facility.objects.filter(id=id).first()
        facility_details_data = FacilityListSerializer(facility_details_data).data
        return Response(facility_details_data)


