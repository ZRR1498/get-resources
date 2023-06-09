# Generated by Django 4.2 on 2023-04-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(unique=True, verbose_name='Date event')),
            ],
            options={
                'verbose_name': 'Event',
                'ordering': ['-date'],
            },
        ),
    ]
