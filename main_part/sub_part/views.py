from django.shortcuts import render
from . models import *
from django.contrib import messages
import datetime

from django.conf import settings
from django.core.mail import send_mail

from rest_framework import generics
from .models import *
from . serializers import MyModelSerializers

class MyModelListCreate(generics.ListCreateAPIView):
    queryset = book_appoinment_table.objects.all()
    serializer_class = MyModelSerializers


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def bookappoinment(request):
    return render(request,'bookappoinment.html')
def register(request):
    return render(request,'register.html')
def service(request):
    return render(request,'service.html')
def about(request):
    return render(request,'about.html')
def dashboard(request):
    return render(request,'dashboard.html')

def book_appoinment_form_submission(request):
    first_name=request.POST.get('first_name')
    print(f"firstname is {first_name}")
    last_name=request.POST.get('last_name')
    print(f"lastname is {last_name}")
    email_id=request.POST.get('email_id')
    print(f"email id is {email_id}")
    mobile_no=request.POST.get('mobile_no')
    print(f"mobile no is {mobile_no}")
    appoinment_date=request.POST.get('appoinment_date')
    print(f"appoinment date is {appoinment_date}")
    

    if book_appoinment_table.objects.filter(email_id=request.POST.get('email_id'),appoinment_date=request.POST.get('appoinment_date')):
        print("***This person has already booked***")
        messages.error(request,'sorry!...already booked',extra_tags='already')
        return render(request,'index.html')
    else:
        booking_datetime=datetime.datetime.now()
        print(f"booking date and time is->{booking_datetime}")

        ex1=book_appoinment_table(first_name=first_name,
                              last_name=last_name,
                              email_id=email_id,
                              mobile_no=mobile_no,
                              appoinment_date=appoinment_date,
                              booking_datetime=booking_datetime)
        ex1.save()
        messages.error(request,'booked successfully!..',extra_tags='booked')
        print("***Appoinment data saved successfully***")
        
        try:
            subject = 'welcome to GFG world'
            message = f'Hi {first_name} {last_name},\your appoinment booking successfully.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_id, ]
            send_mail( subject, message, email_from, recipient_list )
            print("**Mail sent successfully**")
        except:
            print("**Mail not send**")
        return render(request,'index.html')

def login_form_submission(request):
    username=request.POST.get('username')
    print(f"username is {username}")
    password=request.POST.get('password')
    print(f"password is {password}")

    if admin_table.objects.filter(username=username,password=password):
        print("***login successfully***")
        logger_data=admin_table.objects.get(username=username,password=password)
        view_data=book_appoinment_table.objects.all()
        return render(request,'dashboard.html',{'logger_data':logger_data,'view_data':view_data})
    else:
        print("***login failed***")
        messages.error(request,'Invalid username or password!...',extra_tags='login_faild')
        return render(request,"login.html")

def confimation_mail_send(request,user_id):
    user_id=user_id
    print(f"user user_id {user_id}")
    particular_user_data=book_appoinment_table.objects.get(id=user_id)
    
    print(f"firstname is {particular_user_data.first_name}")
    print(f"lastname is {particular_user_data.last_name}")
    print(f"email id is {particular_user_data.email_id}")
    print(f"appoinment date {particular_user_data.appoinment_date}")

#mail code
    try: 
        subject = 'APPOINMENT CONFIRMATION'
        message = f'Hi {particular_user_data.first_name} {particular_user_data.last_name},\n confirmed your appoinment successfuly,\npls come tuesday afternoon 2pm'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [particular_user_data.email_id, ]
        send_mail( subject, message, email_from, recipient_list )
        print("**mail sent successfully***")
        messages.error(request,'mail sent successfully',extra_tags='mail_sent')
    except:
        print("***mail not sent***")

    view_data=book_appoinment_table.objects.all()
    return render(request,'dashboard.html',{'view_data':view_data})