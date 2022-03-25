from django.db import models
from .string import gender_choice, religion_choice, blood_group_choice, class_choice, section_choice
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from School_Management.models import TeacherManagementModel, time_info
# from Teachers.models import Teacher


class Student(TeacherManagementModel):

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=gender_choice, null=True, blank=True)
    religion = models.CharField(max_length=10, choices=religion_choice, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    blood_group = models.CharField(max_length=4, choices=blood_group_choice, default="none", null=True, blank=True)
    nationality = models.CharField(max_length=50, default="Bangladeshi")
    profile_picture = models.ImageField(upload_to="student/profile_pic", null=True, blank=True)
    fee = models.PositiveIntegerField(null=True, blank=True)
    otp = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.full_name+"/"+self.phone


class ClassInfo(TeacherManagementModel):

    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name="Class_info")
    Class = models.CharField(max_length=2, choices=class_choice)
    roll = models.PositiveIntegerField()
    section = models.CharField(max_length=1, choices=section_choice)
    admission_date = models.DateField()

    def __str__(self):
        return self.student.full_name+' - '+str(self.Class)


class GuardianInfo(TeacherManagementModel):

    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name="Guardian_Info")
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    NID_card = models.CharField(max_length=13)
    blood_group = models.CharField(max_length=4, choices=blood_group_choice, default="none")

    def __str__(self):
        return self.student.full_name + ", " + self.full_name


class StudentPost(TeacherManagementModel):

    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    post_picture = models.ImageField(upload_to="student/post", null=True, blank=True)
    post_text = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.post_text:
            return self.post_text
        else:
            return str(self.user)


class PostLike(TeacherManagementModel):

    post = models.ForeignKey(StudentPost, on_delete=models.PROTECT, related_name="user_post")
    user = models.ForeignKey(User, on_delete=models.PROTECT)

pre_save.connect(time_info, sender=StudentPost)
pre_save.connect(time_info, sender=Student)
pre_save.connect(time_info, sender=ClassInfo)
pre_save.connect(time_info, sender=GuardianInfo)
