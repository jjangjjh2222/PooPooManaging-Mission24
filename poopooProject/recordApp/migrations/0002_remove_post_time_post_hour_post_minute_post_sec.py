# Generated by Django 4.1 on 2022-08-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
        migrations.AddField(
            model_name='post',
            name='hour',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='minute',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sec',
            field=models.IntegerField(null=True),
        ),
    ]
