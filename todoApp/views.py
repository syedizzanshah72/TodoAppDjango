from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationform
from django.contrib.auth import login ,logout,authenticate

from .forms import todoForm
from .models import TodoModel
# Create your views here.
@login_required
def todo(request):
    if request.method == "POST":
        form = todoForm(request.POST)
        if form.is_valid():
            todo_obj = form.save(commit=False)
            # user.set_password(form.cleaned_data['password1'])
            todo_obj.user = request.user
            todo_obj.save()
            form = todoForm()
            # login(request,user)
    else:
            form = todoForm()
    return render(request,"todo.html",{'form':form})




def Registration(request):
    if request.method == "POST":
        form = UserRegistrationform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('todo.html')
    else:
            form = UserRegistrationform()
    return render(request,"Registration/register.html",{'form':form})

def display(request):
    data = TodoModel.objects.all()
    return render('request','todo.html',{'data':data})


# def login(request):
#     if request.method == "POST":
#           username = request.POST.get('username')
#           password = request.POST.get('password')
#           user = authenticate(request,username=username,password=password)

#           if user is not None:
#             login(request,user)
#             return redirect('todo.html')
#           else:
#             return render(request, "Registration/login.html", {'error': 'Invalid credentials'})
#     return render(request, "Registration/login.html")