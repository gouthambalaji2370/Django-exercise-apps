from django.shortcuts import render


# Create your views here.

def renderTemplate(request):
    myDict = {"name": "gouthambalaji"}
    return render(request, 'templateApp/firstTemplate.html', context=myDict)

def renderEmployee(request):
    myEmployeeDict = {"id": 123, "name": "john", "salary": 10000}
    return render(request, 'templateApp/employeeTemplate.html', myEmployeeDict)