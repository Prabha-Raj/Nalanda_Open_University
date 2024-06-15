from django.contrib import admin
from . models import Student,Login,Enquiry,Email

# Register your models here.
admin.site.register(Student)
admin.site.register(Login)
admin.site.register(Enquiry)
admin.site.register(Email)