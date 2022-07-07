# Generated by Django 2.1.7 on 2022-07-06 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_application_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='applicant',
        ),
        migrations.RemoveField(
            model_name='application',
            name='job',
        ),
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='image',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]