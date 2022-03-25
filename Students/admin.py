from django.contrib import admin
from .models import Student, ClassInfo, GuardianInfo, StudentPost

class StudentAdmin(admin.ModelAdmin):
    fields = ["full_name", "profile_picture", "father_name", "mother_name", "gender", "religion", "birth_date", "email",
              "phone", "address", "blood_group", "nationality", "otp"]

    list_display = [
        "full_name",
        "user",
        "create_at",
        "modified_at"
    ]
admin.site.register(Student,StudentAdmin)

class ClassInfoAdmin(admin.ModelAdmin):
    fields = [
        "student",
        ("Class", "roll"),
        "section",
        "admission_date"
    ]

    list_display = [
        "student", "Class", "roll", "create_at",
        "modified_at"
    ]
admin.site.register(ClassInfo,ClassInfoAdmin)

class GuardianInfoAdmin(admin.ModelAdmin):
    fields = [
        "student",
        ("full_name", "blood_group"),
        "phone",
        "NID_card"
    ]
    list_display = ["student", "full_name", "phone", "create_at", "modified_at"]
admin.site.register(GuardianInfo,GuardianInfoAdmin)

class StudentPostAdmin(admin.ModelAdmin):
    fields = [
        "user",
        "post_picture",
        "post_text",
    ]
    list_display = [
        "user",
        "post_text",
        "id",
        "create_at",
        "modified_at"
    ]
admin.site.register(StudentPost,StudentPostAdmin)
