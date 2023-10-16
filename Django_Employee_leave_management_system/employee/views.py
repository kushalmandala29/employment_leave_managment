from django.shortcuts import render, redirect
from .models import employee_details, leave_request
from .forms import leaving_apply
from django.contrib import messages
# Create your views here.


def employee_login(request):
    if request.method == "POST":
        # get email and password from template
        log_email=request.POST.get('log_email')
        log_password=request.POST.get('log_password')

        # check the email that is have in database or not.
        check_filter_employee = employee_details.objects.filter(email=log_email)

        # if the email is valid
        if check_filter_employee:
            # get the info of the employee by email
            get_employee = employee_details.objects.get(email=log_email)

            employee_password=get_employee.password
            # now matching password
            # if password matched:
            if log_password==employee_password:
                #start login session of instructor
                request.session['employee_id'] = get_employee.id
                request.session['employee_first_name'] = get_employee.first_name
                request.session['employee_last_name'] = get_employee.last_name
                request.session['employee_email'] = get_employee.email
                return redirect('index')
            else:
                # else show error.
                erorr_message_2 = "Password is Wrong, Please Try Again !!"
                value_func2 = {'erorr_message_2': erorr_message_2, 'log_email': log_email}
                return render(request, 'employee_login.html', value_func2)
        else:
            # else show error.
            erorr_message_2 = "Email is Wrong, Please Try Again !!"
            value_func2 = {'erorr_message_2': erorr_message_2, 'log_email': log_email}
            return render(request, 'employee_login.html', value_func2)
    return render(request, 'employee_login.html')


def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def leave_apply(request):
    employee_id = request.session.get('employee_id')
    get_employee = employee_details.objects.get(id=employee_id)
    form = leaving_apply()

    if request.method == 'POST':
        form = leaving_apply(request.POST)
        if form.is_valid():
            employee_request = form.save(commit=False)
            employee_request.Employee=get_employee
            employee_request.save()
            messages.success(request, 'Your Request For leave has been sent to Admin !!')
            return redirect('leave_apply')

    CONTEXT={
        'form':form
    }
    return render(request, 'leave_apply.html', CONTEXT)


def see_leave_application(request):
    employee_id = request.session.get('employee_id')
    get_employee = employee_details.objects.get(id=employee_id)

    leave_request_filter = leave_request.objects.filter(Employee=get_employee).order_by('-id')

    CONTEXT2={'leave_request_filter':leave_request_filter}

    return render(request, 'see_leave_application.html', CONTEXT2)

def logout_func(request):
    request.session.clear()
    return redirect('index')