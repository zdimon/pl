# Generated by Django 3.0.7 on 2020-09-11 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20200911_0839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='lessons',
            new_name='lesson',
        ),
    ]
