from django.db import models
from School_Management.models import TeacherManagementModel, time_info
from django.db.models.signals import pre_save
class FooterData(TeacherManagementModel):

    # copyright()
    year = models.CharField(max_length=4)
    copyright_owner = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.year

pre_save.connect(time_info, sender=FooterData)

