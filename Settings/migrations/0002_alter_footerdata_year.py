# Generated by Django 4.0.1 on 2022-03-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerdata',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
