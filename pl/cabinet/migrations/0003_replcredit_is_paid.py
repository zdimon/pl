# Generated by Django 3.0.7 on 2020-09-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0002_replcredit'),
    ]

    operations = [
        migrations.AddField(
            model_name='replcredit',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
