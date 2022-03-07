from django.shortcuts import render
from empApp.models import Employee,Passenger


# Create your views here.


def employeedata(request):
    employees = Employee.objects.all()
    empDict = {'employees': employees}
    return render(request, 'empApp/employees.html', empDict)


def passengerdata(request):
    passenger = Passenger.objects.all()
    passDict = {'passengers': passenger}
    return render(request, 'empApp/passenger.html', passDict)
