from django.contrib import admin
from empApp.models import Employee,Passenger


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'salary', 'email']

class PassengerAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'email', 'rewardPoints']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Passenger, PassengerAdmin)
