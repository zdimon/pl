# Generated by Django 3.0.7 on 2020-07-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_article_catalog'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='meta_keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
