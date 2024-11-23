from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.views.generic.edit import FormMixin
from django.views.generic import ListView ,DetailView ,CreateView
from django.db.models.query_utils import Q
from django_filters.views import FilterView

################################

from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.



# class User (AbstractUser):
#     is_admin = models.BooleanField('Isadmin', default= False)
#     is_customer = models.BooleanField('Iscustomer', default=False)
#     is_employee = models.BooleanField('Isemployee', default=False)


class Doctor01(models.Model):

    c = [("Geriatric_medicine_doctors","Geriatric_medicine_doctors"), ("Infectious_disease_doctors","Infectious_disease_doctors"), ("Urologists","Urologists"), ("Neurologists","Neurologists"), ("General_surgeons","General_surgeons"), ("Cardiac_surgeons","Cardiac_surgeons"), ("Orthopedic_surgeons","Orthopedic_surgeons")]
    f_name = models.CharField(max_length=10, null = True, blank= True)
    l_name = models.CharField(max_length=10, null = True, blank= True)
    full_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='doctor01/%y/%m/%d')
    content = models.TextField(null = True, blank= True)
    category = models.CharField(max_length=50, null=True, blank=True, choices = c)
    added_at = models.DateTimeField(null = True)
    active = models.BooleanField(default = False)

    def __str__(self):
        return self.full_name




class Patient01(models.Model):
    f_name = models.CharField(max_length=10, null = True, blank= True)
    l_name = models.CharField(max_length=10, null = True, blank= True)
    full_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    image = models.ImageField(upload_to='patient01/%y/%m/%d')
    added_at = models.DateTimeField(default = datetime.now)



    def __str__(self):
        return self.full_name

##################################################


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor/')
    specialty = models.TextField(max_length=10000)
    phone_number = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('doctor_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Doctor, self).save(*args, **kwargs)



########################################################


class DoctorBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    civil_id = models.CharField(max_length=16)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=True)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()

            return redirect('')





    ########################################################

# for the payment


class Product(models.Model):
    name = models.CharField (max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order (models.Model):
    order_id = models.IntegerField()
    order_completed = models.BooleanField(default= False)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)


    def __str__(self):
        return str(self.order_id)








