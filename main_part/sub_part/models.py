from django.db import models

# Create your models here.

class book_appoinment_table(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    mobile_no=models.CharField(max_length=15)
    appoinment_date=models.CharField(max_length=100)
    booking_datetime=models.CharField(max_length=100)

class admin_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)