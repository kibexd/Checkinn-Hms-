# Generated by Django 3.0.3 on 2020-03-05 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_rooms_room_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booked_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]