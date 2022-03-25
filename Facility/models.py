from django.db import models
from School_Management.models import TeacherManagementModel, time_info
from django.db.models.signals import pre_save

class Facility(TeacherManagementModel):

    facility_name = models.CharField(max_length=100)
    facility_image = models.ImageField(upload_to="facility/image")
    facility_details = models.TextField()

pre_save.connect(time_info, sender=Facility)