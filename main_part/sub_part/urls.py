from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('book_appoinment_form_submission',views.book_appoinment_form_submission,name='book_appoinment_form_submission'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('login_form_submission',views.login_form_submission,name='login_form_submission'),
    path('confimation_mail_send/<int:user_id>',views.confimation_mail_send,name='confimation_mail_send'),
    path('api/book_appoinment_table/',views.MyModelListCreate.as_view(),name='mymodel-list'),
]