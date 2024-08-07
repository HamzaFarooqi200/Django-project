# Generated by Django 3.2.12 on 2024-08-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_student_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('practice.student',),
        ),
        migrations.CreateModel(
            name='Sportsman',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('practice.student',),
        ),
        migrations.AddField(
            model_name='student',
            name='is_speaker',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_sportsman',
            field=models.BooleanField(default=False),
        ),
    ]
