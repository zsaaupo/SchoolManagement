# Generated by Django 4.0.1 on 2022-02-27 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0009_studentpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Class_info', to='Students.student'),
        ),
        migrations.AlterField(
            model_name='guardianinfo',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Guardian_Info', to='Students.student'),
        ),
    ]