# Generated by Django 5.0.2 on 2024-03-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0002_book_appoinment_table_booking_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
