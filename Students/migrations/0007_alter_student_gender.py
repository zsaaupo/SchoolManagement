# Generated by Django 4.0 on 2022-02-10 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0006_alter_student_blood_group_alter_student_father_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Other')], max_length=6, null=True),
        ),
    ]