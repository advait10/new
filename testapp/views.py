from django.shortcuts import render, redirect
from .models import Employee
from testapp.form import Employee_Reg


def welcome(request):
    form = Employee_Reg()
    emp = Employee.objects.all()
    return render(request, 'sd.html', {'form': form, 'emp': emp})


def save_data(request):
    form = Employee_Reg()
    if request.method == 'POST':
        form = Employee_Reg(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'sd.html', {'form': form})


def delete_stud(request, id):
    form = Employee_Reg()
    stud = Employee.objects.get(id=id)
    if stud:
        stud.delete()
        msg = 'Employee Deleted Successfully'
    else:
        msg = 'Employee Not Found'
    form = Employee_Reg()
    emp = Employee.objects.all()
    return render(request, 'sd.html', {'form': form, 'emp': emp, 'msg': msg})


def update_stud(request, id):
    msg = "hello"
    emp = Employee.objects.get(id=id)
    if request.method == 'POST':
        print('inside POST')
        form = Employee_Reg(request.POST, instance=emp)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/wel/')
    return render(request, 'update.html', {'msg': msg, 'emps': emp})
