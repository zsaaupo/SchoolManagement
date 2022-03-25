from django.db import models
from .string import gender_choice, religion_choice, blood_group_choice, marital_status_choice, scale_choice, position_choice
from School_Management.models import TeacherManagementModel, time_info
from django.db.models.signals import pre_save
from Students.models import Student

class Teacher(TeacherManagementModel):

    full_name = models.CharField(max_length=100)
    Position = models.CharField(max_length=20, choices=position_choice, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=gender_choice)
    religion = models.CharField(max_length=10, choices=religion_choice)
    birth_date = models.DateField()
    marital_status = models.CharField(max_length=10, null=True, blank=True, choices=marital_status_choice)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    address = models.TextField()
    blood_group = models.CharField(max_length=4, choices=blood_group_choice, default="none")
    nationality = models.CharField(max_length=50, default="Bangladeshi")
    profile_picture = models.ImageField(upload_to="teacher/profile_pic", null=True, blank=True)
    # student = models.ManyToManyField(Student,null= True, blank=True)

    def __str__(self):
        return self.full_name

class TeacherEducation(TeacherManagementModel):

    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name="Teacher_Education")
    certificate = models.CharField(max_length=100)
    result = models.CharField(max_length=20)
    On_a_scale_of = models.CharField(max_length=20, choices=scale_choice)
    institute = models.CharField(max_length=50)
    board = models.CharField(max_length=15, null=True, blank=True)
    passing_year = models.CharField(max_length=4)

    def __str__(self):
        return self.teacher.full_name+" ("+self.certificate+")"

class TeacherExperience(TeacherManagementModel):

    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name="Teacher_Experience")
    job_title = models.CharField(max_length=50)
    joining_date = models.DateField()
    leaving_date = models.DateField()
    job_detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.teacher.full_name + " (" + self.job_title + ")"

pre_save.connect(time_info, sender=Teacher)
pre_save.connect(time_info, sender=TeacherEducation)
pre_save.connect(time_info, sender=TeacherExperience)