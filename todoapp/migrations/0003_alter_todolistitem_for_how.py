# Generated by Django 3.2.2 on 2021-05-13 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_repo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistitem',
            name='for_how',
            field=models.CharField(blank=True, max_length=55),
        ),
    ]
