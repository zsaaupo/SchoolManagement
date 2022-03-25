from rest_framework import serializers
from .models import Facility

class FacilityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ["id", "facility_name", "facility_image", "facility_details"]
