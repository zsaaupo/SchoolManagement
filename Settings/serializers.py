from rest_framework import serializers
from .models import FooterData

class FooterDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = FooterData
        fields = ["id", "year", "copyright_owner", "phone"]