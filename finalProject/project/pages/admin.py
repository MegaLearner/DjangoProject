from django.contrib import admin
from .models import Doctor01, Patient01, Doctor, DoctorBook, Order, Product


# Register your models here.

admin.site.register(Doctor01)
admin.site.register(Patient01)

admin.site.register(Doctor)
admin.site.register(DoctorBook)
admin.site.register(Product)
admin.site.register(Order)




