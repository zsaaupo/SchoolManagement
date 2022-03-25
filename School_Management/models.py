from django.db import models
from django.utils import timezone
class TeacherManagementModel(models.Model):

    create_by = models.CharField(max_length=255, null=True)
    create_at = models.DateField(null=True)
    create_from = models.CharField(max_length=255, null=True)
    modified_by = models.CharField(max_length=255, null=True)
    modified_at = models.DateField(null=True)
    modified_from = models.CharField(max_length=255, null=True)
    is_archived = models.BooleanField(default=False)
    archived_by = models.CharField(max_length=255, null=True)
    archived_at = models.DateField(null=True)
    archived_from = models.CharField(max_length=255, null=True)

    class Meta:

        abstract = True

def time_info(sender, instance, *agrs, **kwargs):
    if instance._state.adding:
        instance.create_at = timezone.now()
    else:
        instance.modified_at = timezone.now()
        if instance.is_archived and not instance.archived_at:
            instance.archived_at = timezone.now()