# Generated by Django 4.0.4 on 2022-05-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful_apis', '0004_progress_departmentgoalname'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='endDate',
            field=models.DateField(null=True),
        ),
    ]
