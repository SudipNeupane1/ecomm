from django.contrib.auth import authenticate,login,get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import ContactForm,LoginForm,RegisterForm

def home(request):
    context ={
        "title":"hello world!",
        "content":"welcome to the homepage",
    }
    if request.user.is_authenticated:
        context["Premium_content"]="YEAHHHH"
    return render(request,"home.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context  = {
        "title":"Contact",
        "content":"welcome to the contact page",
        "form":contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,"contact/view.html",context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    print("User logged in")
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        usr = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            print("Error")
    return render(request,"auth/login.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.object.create_user(username,email,password)
        print(new_user)
    
    return render(request,"auth/register.html",context)

