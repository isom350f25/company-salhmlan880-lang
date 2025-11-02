# Create your views here.
from django.shortcuts import render
from .models import employee  

def employee_list(request):
    employees = employee.objects.all().order_by('name')  
    return render(request, 'employee_list.html', {'employees': employees})
