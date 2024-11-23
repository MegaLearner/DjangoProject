from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# from .forms import LoginForm, RegisterForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .middlewares import auth, guest
from .models import Doctor01
############################################
from .models import Doctor, Product, Order
from django_filters.views import FilterView

from django.views.generic.edit import FormMixin
from django.views.generic import ListView ,DetailView ,CreateView
from .forms import DoctorBookForm
from django.db.models.query_utils import Q
from django.urls import reverse

############################################

# Create your views here.

def index (request):
    return render(request, 'pages/index.html')

def about (request):
    return render(request, 'pages/about.html')

def appointment (request):
    return render(request, 'pages/appointment.html')

def contact (request):
    return render(request, 'pages/contact.html')

def payment (request):
    return render(request, 'pages/payment.html')

def paymentd (request, id):
    product = Product.objects.get(id= id)
    return render(request, 'pages/paymentd.html', {'product':product})

@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('pages/dashboard')
    else:
        initial_data = {'username':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'pages/signup.html',{'form':form})

############################################


@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('pages/dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'pages/login.html',{'form':form})



############################################

@auth
def dashboard_view(request):
    return render(request, 'pages/dashboard.html')



def logout_view(request):
    logout(request)
    return redirect('pages/login')



############################################

def doctors (request):
    return render(request, 'pages/doctors.html')

def doctor01 (request):

    Doctor01.objects.all()


    return render(request, 'pages/doctor01.html', {'D': Doctor01.objects.all()})
 ############################################################33

# class DoctorList (ListView):
#     model = Doctor
#     paginate_by = 1
#     template_name = 'pages/doctor_list.html'
#
#
# class DoctorDetail(FormMixin, DetailView):
#
#     model = Doctor
#     form_class = DoctorBookForm
#     template_name = 'pages/doctor_detail.html'
#
#     def get_queryset(self):
#         name = self.request.GET.get('q', '')
#         object_list = Doctor.objects.filter(
#             Q(name__icontains=name) |
#             Q(specialty__icontains=name)
#         )
#         return object_list

####################################################################



    ###########################################

def patient01 (request):
    return render(request, 'pages/patient01.html')


def service (request):
    return render(request, 'pages/service.html')

def map (request):
    return render(request, 'pages/map.html')
