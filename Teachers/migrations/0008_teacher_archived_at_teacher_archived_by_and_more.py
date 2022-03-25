# Generated by Django 4.0 on 2022-01-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0007_teacher_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='archived_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='archived_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='archived_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='create_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='create_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='create_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='modified_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teachereducation',
            name='archived_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='teachereducation',
            name='archived_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teachereducation',
            name='archived_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teachereducation',
            name='create_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='teachereducation',
            name='create_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teachereducation',
            name='create_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teachereducation',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teachereducation',
            name='modified_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='teachereducation',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teachereducation',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacherexperience',
            name='archived_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='teacherexperience',
            name='archived_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacherexperience',
            name='archived_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacherexperience',
            name='create_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='teacherexperience',
            name='create_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacherexperience',
            name='create_from',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacherexperience',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacherexperience',
            name='modified_at',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='teacherexperience',
            name='modified_by',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacherexperience',
            name='modified_from',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
