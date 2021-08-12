# Generated by Django 3.2.6 on 2021-08-12 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(max_length=100, verbose_name='Occupation')),
                ('posts', models.IntegerField(max_length=4, verbose_name='Positions Available')),
                ('sector', models.CharField(max_length=100, verbose_name='Job Domain')),
                ('organization', models.CharField(max_length=60, verbose_name='Organization Name')),
                ('Location', models.CharField(max_length=20, verbose_name='Area Found')),
                ('mode', models.CharField(choices=[('FT', 'Full Time'), ('PT', 'Part Time')], max_length=15)),
                ('description', models.TextField(verbose_name='Job Description')),
                ('posted_on', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('deadline', models.DateField(verbose_name='Deadline')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
