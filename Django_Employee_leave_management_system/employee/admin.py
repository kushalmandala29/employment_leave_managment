from django.contrib import admin
from .models import employee_details, leave_request
# Register your models here.


admin.site.register(employee_details)
admin.site.register(leave_request)