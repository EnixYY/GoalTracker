# Generated by Django 4.0.4 on 2022-05-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful_apis', '0003_departmentgoals_totalusercontribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='departmentGoalName',
            field=models.CharField(max_length=300, null=True),
        ),
    ]