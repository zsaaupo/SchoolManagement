from django.contrib import admin
from .models import Teacher, TeacherEducation, TeacherExperience
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, SimpleListFilter, AllValuesFieldListFilter, ChoicesFieldListFilter, RelatedFieldListFilter, RelatedOnlyFieldListFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

class TeacherAdmin(admin.ModelAdmin):
    # filter_horizontal = ('student',)
    def get_queryset(self, request):
        queryset = Teacher.objects.filter(is_archived=False).all()
        # queryset2 = Teacher.objects.filter().order_by('id')
        return queryset
    fields = [
        "full_name",
        "Position",
        ("gender", "religion"),
        ("birth_date", "marital_status"),
        ("email", "phone"),
        "address",
        ("blood_group", "nationality"),
        "profile_picture",
        "is_archived"
    ]
    list_filter = (
        ('gender', AllValuesFieldListFilter),
        ('modified_at', DateRangeFilter),
    )
    list_display = ["full_name", "Position", "email", "phone", "create_at", "modified_at"]
    list_per_page = 5

admin.site.register(Teacher,TeacherAdmin)


class TeacherEducationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = TeacherEducation.objects.filter(teacher__is_archived=False).all()
        # queryset2 = Teacher.objects.filter().order_by('id')
        return queryset
    fields = [
        "teacher",
        "certificate",
        ("result", "On_a_scale_of"),
        ("institute", "board"),
        "passing_year",
        "is_archived"
    ]
    list_filter = (
        ('teacher', RelatedDropdownFilter),
        ('modified_at', DateTimeRangeFilter),
    )
    list_display = ["teacher", "certificate", "create_at", "modified_at", "is_archived"]
    list_per_page = 5

admin.site.register(TeacherEducation, TeacherEducationAdmin)


class TeacherExperienceAdmin(admin.ModelAdmin):

    fields = [
        "teacher",
        "job_title",
        ("joining_date", "leaving_date"),
        "job_detail"
    ]
    list_display = ["teacher", "job_title", "create_at", "modified_at"]
    list_per_page = 5

admin.site.register(TeacherExperience, TeacherExperienceAdmin)
