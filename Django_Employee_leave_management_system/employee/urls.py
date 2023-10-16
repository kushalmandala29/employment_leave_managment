
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('employee-login', views.employee_login, name="employee_login"),
    path('profile', views.profile, name="profile"),
    path('leave_apply', views.leave_apply, name="leave_apply"),
    path('see_leave_application', views.see_leave_application, name="see_leave_application"),
    path('logout_func', views.logout_func, name="logout_func"),
]