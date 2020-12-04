from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from room.models import Room
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from room.forms import RoomForm


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def home(request):
    data = Room.objects.all()[::-1]
    context = {
        'room':data
    }
    return render(request,'home.html',context)


def views_more(request,id):
    data = Room.objects.get(pk=id)
    context = {
        'room':data
    }
    return render(request,'views_more.html',context)
#
# def signup(request):
#     if request.method=='GET':
#         return render(request,'signup.html')
#     else:
#         u = request.POST['username']
#         e = request.POST.get('email')
#         p1 = request.POST['pass1']
#         p2 = request.POST['pass2']
#
#         if p1==p2:
#             try:
#                 u = User(username=u,email=e)
#                 u.set_password(p1)
#                 u.save()
#             except:
#                 messages.add_message(request,messages.ERROR,"Username already exist")
#                 return redirect('signup')
#             messages.add_message(request,messages.SUCCESS,"signup success")
#             return redirect('signin')
#         else:
#             messages.add_message(request,messages.ERROR,"password does not match")
#             return redirect('signup')

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u = request.POST['username']
        p = request.POST['pass1']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "password does not match")
            return redirect('signin')


def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def dashboard(request):
    data = Room.objects.all()[::-1]
    context = {
        'room':data
    }
    return render(request,'dashboard.html',context)

@login_required(login_url='signin')
def create_post(request):
    form = RoomForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Created successfully")
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request,'create_post.html',context)

@login_required(login_url='signin')
def edit_post(request,id):
    data = Room.objects.get(pk=id)
    form = RoomForm(request.POST or None,request.FILES or None,instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"update successfully")
        return redirect('dashboard')
    context = {
        'form':form
    }
    return render(request,'edit_post.html',context)

@login_required(login_url='signin')
def delete_post(request,id):
    b = Room.objects.get(pk=id)
    b.delete()
    messages.add_message(request,messages.SUCCESS,"successfully deleted")
    return redirect('dashboard')
