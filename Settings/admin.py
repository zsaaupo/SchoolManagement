from django.contrib import admin
from .models import FooterData

class FooterDataAdmin(admin.ModelAdmin):

    fields = ["year", "copyright_owner", "phone"]
    list_display = ["year", "copyright_owner", "phone", "create_at", "modified_at"]

admin.site.register(FooterData,FooterDataAdmin)