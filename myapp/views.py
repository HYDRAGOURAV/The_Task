from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import User,Task
def main_Page(req):
    return render(req,"index.html")
def add_User(req):
    if req.method == "POST":
        name = req.POST.get("name")
        email = req.POST.get("email")
        mobile = req.POST.get("Mobile")
        length = len(mobile)
        if length==10:
            UserData =  User(name=name, email = email , mobile = mobile)
            if UserData.isExists():
                messages.warning(req,"Email already Registered")
                return  render(req,"index.html")
            else:
                UserData.save()
                messages.success(req,"User Added Successfully")
                return render(req,"index.html")
        else:
            messages.warning(req,"Mobile number should be 10 digit")
            return render(req,"index.html")

    return render(req,"index.html")

def task_details(req):
    The_Data = User.objects.all()
    task_Data = Task.objects.all()
    context = {
        'The_Data':The_Data,
        'task_Data':task_Data,
    }
    return render(req,"Task_Page.html",context)
def see_task(req,user_id):
    The_user_task = User.objects.get(user_id= user_id)
    The_Task = Task.objects.get(user_id = user_id)

    the_user_data = {
        'The_user_task':The_user_task,
        'The_Task':The_Task,
    }
    return render(req,"Task_show.html",the_user_data)

