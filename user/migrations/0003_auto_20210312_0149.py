# Generated by Django 3.1.7 on 2021-03-12 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210312_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
