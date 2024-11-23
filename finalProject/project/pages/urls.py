from django.urls import path
from . import views
# from .views import DoctorList, DoctorDetail


urlpatterns = [
    path('', views.index, name= 'index'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact'),
    path('appointment/', views.appointment, name= 'appointment'),
    path('payment/', views.payment, name= 'payment'),
    path('paymentd/<int:id>', views.paymentd, name='paymentd'),
    path('signup/', views.register_view, name= 'signup'),
    path('doctors/', views.doctors, name= 'doctors'),
    path('service/', views.service, name='service'),
    path('login/', views.login_view, name= 'login'),
    path('map/', views.map, name='map_url'),
    path('dashboard/', views.dashboard_view, name= 'dashboard'),
    path('doctor01/', views.doctor01, name='doctor01'),
    ##################################################
    # path('doctor_list/', DoctorList.as_view(), name='doctor_list'),
    # path('<slug:slug>', DoctorDetail.as_view(), name='doctor_detail'),
]