# Generated by Django 5.0.2 on 2024-03-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_appoinment_table',
            name='booking_datetime',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
