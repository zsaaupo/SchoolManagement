from django.contrib import admin
from .models import Facility


class FacilityAdmin(admin.ModelAdmin):

    fields = [
        "facility_name",
        "facility_image",
        "facility_details"
    ]
    list_display = [
        "facility_name",
        "facility_image",
        "facility_details",
        "create_at",
        "modified_at"
    ]

admin.site.register(Facility,FacilityAdmin)
