# Generated by Django 4.0.4 on 2022-05-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful_apis', '0002_alter_progress_employeeinput_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='departmentgoals',
            name='totalUserContribution',
            field=models.IntegerField(null=True),
        ),
    ]
