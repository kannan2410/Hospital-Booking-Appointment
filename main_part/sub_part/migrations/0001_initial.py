# Generated by Django 5.0.2 on 2024-02-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_appoinment_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
                ('mobile_no', models.CharField(max_length=15)),
                ('appoinment_date', models.CharField(max_length=100)),
            ],
        ),
    ]
