# Generated by Django 3.0.7 on 2021-02-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_topic_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='created_at',
            field=models.DateField(default='2000-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_at',
            field=models.DateField(),
        ),
    ]
