# Generated by Django 3.0.7 on 2020-07-10 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20200709_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='Name')),
                ('number', models.IntegerField(blank=True, verbose_name='Number')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is main?')),
                ('image', models.ImageField(blank=True, null=True, upload_to='lessons_images', verbose_name='Image')),
                ('name_slug', models.CharField(blank=True, max_length=250, verbose_name='Name slug')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='Course')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, verbose_name='Name')),
                ('filename', models.CharField(blank=True, max_length=250, verbose_name='Name slug')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Lesson', verbose_name='Lesson')),
            ],
        ),
    ]
