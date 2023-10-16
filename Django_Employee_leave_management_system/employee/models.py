from django.db import models
from datetime import datetime
# Create your models here.


class employee_details(models.Model):
    class Meta:
        verbose_name_plural = 'Employee Details'

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name


class leave_request(models.Model):
    class Meta:
        verbose_name_plural = 'Leave Requests'

    Employee = models.ForeignKey(employee_details, on_delete=models.CASCADE)
    Subject = models.CharField(max_length=300)
    Reason = models.TextField()
    Request_time = models.DateTimeField(default=datetime.now())
    Status=(('Progressing', "Progressing"),
                    ('Accepted', "Accepted"),
                    ('Rejected', "Rejected"))
    Request_Status=models.CharField(max_length=100, choices=Status, default="Progressing")

    def __str__(self):
        return self.Employee.first_name + " " + self.Employee.last_name
