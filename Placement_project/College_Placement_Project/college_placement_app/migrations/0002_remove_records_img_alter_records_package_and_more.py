# Generated by Django 4.0.2 on 2022-02-25 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_placement_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='records',
            name='img',
        ),
        migrations.AlterField(
            model_name='records',
            name='package',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='records',
            name='year',
            field=models.IntegerField(),
        ),
    ]
