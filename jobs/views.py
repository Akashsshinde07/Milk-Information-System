from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                user1 = Applicant.objects.get(user=user)
                if user1.type == "applicant":
                    login(request, user)
                    return redirect("/cattle")
            else:
                thank = True
                return render(request, "login.html", {"thank":thank})
    return render(request, "user_login.html")

def user_homepage(request):
    if not request.user.is_authenticated:
        return redirect('/user_login/')
    applicant = Applicant.objects.get(user=request.user)
    if request.method=="POST":
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        gender = request.POST['gender']

        applicant.user.email = email
        applicant.user.first_name = first_name
        applicant.user.last_name = last_name
        applicant.gender = gender
        applicant.save()
        applicant.user.save()

    return render(request, "user_homepage.html", {'applicant':applicant})

def signup(request):
    if request.method=="POST":   
        username = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        gender = request.POST['gender']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/signup')
        
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1)
        applicants = Applicant.objects.create(user=user, gender=gender, type="applicant")
        user.save()
        applicants.save()
    return render(request, "signup.html")

def Logout(request):
    logout(request)
    return redirect('/')


def welcome(request):
    return render(request, 'welcome.html')

def aaa(request):
    return render(request, 'aaa.html')

def loginpage(request):
    return render(request, 'loginpage.html')



def registerpage(request):
    return render(request, 'registerpage.html')


def forget(request):
    return render(request, 'forget.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def base(request):
    return render(request, 'base.html')


def cattle(request):
    return render(request, 'cattle.html')


def demo(request):
    return render(request, 'demo.html')


def buffalo(request):
    return render(request, 'buffalo.html')


def gir(request):
    return render(request, 'gir cattle2.html')


def result(request):
    return render(request, 'result.html')


def deoni(request):
    return render(request, 'deoni.html')


def deoniresult(request):
    return render(request, 'deoni result.html')


def hariana(request):
    return render(request, 'hariana cattle.html')


def harianaresult(request):
    return render(request, 'hariana cattle result.html')


def krishnavalley(request):
    return render(request, 'krishna valley cattle.html')


def krishnavalleyresult(request):
    return render(request, 'krishna valley cattle result.html')


def murrah(request):
    return render(request, 'murrah buffalo.html')


def murrahresult(request):
    return render(request, 'murrah buffalo result.html')


def bhadawari(request):
    return render(request, 'bhadawari buffalo.html')


def bhadawariresult(request):
    return render(request, 'bhadawari buffalo result.html')


def pandharpuri(request):
    return render(request, 'pandharpuri buffalo.html')


def pandharpuriresult(request):
    return render(request, 'pandharpuri buffalo result.html')


def nagpuri(request):
    return render(request, 'nagpuri buffalo.html')


def nagpuriresult(request):
    return render(request, 'nagpuri buffalo result.html')


def add(request):
    num1 = int(request.GET["num1"])
    res = round(num1 / 20 + 0.09, 2)
    num2 = num1
    res1 = round(num2 / 0.7 - 5, 2)
    num3 = num1
    res2 = round(num3 / 1.09, 2)
    num4 = num1
    res3 = round(num4 / 18 - 0.1, 2)
    num5 = num1
    res4 = round(num5 / 0.7 + 4.4, 2)
    num6 = num1
    res5 = round(num6 / 0.8 + 3.12, 2)
    return render(request, 'result.html',{"Total": num1, "result": res, "result1": res1, "result2": res2, "result3": res3, "result4": res4,"result5": res5})


def add1(request):
    num1 = int(request.GET["num1"])
    res = num1 * 4 * 1 / 100
    num2 = num1
    res1 = round(num2 / 0.7 - 5, 2)
    num3 = num1
    res2 = round(num3 / 1.09, 2)
    num4 = num1
    res3 = round(num4 / 18 - 0.1, 2)
    num5 = num1
    res4 = round(num5 / 0.7 + 4.4, 2)
    num6 = num1
    res5 = round(num6 / 0.8 + 3.12, 2)
    return render(request, 'deoni result.html',
                  {"Total": num1, "result": res, "result1": res1, "result2": res2, "result3": res3, "result4": res4,
                   "result5": res5})


def add2(request):
    num1 = int(request.GET["num1"])
    res = num1 * 4 * 1 / 100
    num2 = num1
    res1 = round(num2 / 0.7 - 5, 2)
    num3 = num1
    res2 = round(num3 / 1.09, 2)
    num4 = num1
    res3 = round(num4 / 18 - 0.1, 2)
    num5 = num1
    res4 = round(num5 / 0.7 + 4.4, 2)
    num6 = num1
    res5 = round(num6 / 0.8 + 3.12, 2)
    return render(request, 'hariana cattle result.html',
                  {"Total": num1, "result": res, "result1": res1, "result2": res2, "result3": res3, "result4": res4,
                   "result5": res5})


def add3(request):
    num1 = int(request.GET["num1"])
    res = num1 * 4 * 1 / 100
    num2 = num1
    res1 = round(num2 / 0.7 - 5, 2)
    num3 = num1
    res2 = round(num3 / 1.09, 2)
    num4 = num1
    res3 = round(num4 / 18 - 0.1, 2)
    num5 = num1
    res4 = round(num5 / 0.7 + 4.4, 2)
    num6 = num1
    res5 = round(num6 / 0.8 + 3.12, 2)
    return render(request, 'krishna valley cattle result.html',
                  {"Total": num1, "result": res, "result1": res1, "result2": res2, "result3": res3, "result4": res4,
                   "result5": res5})


def add4(request):
    num1 = int(request.GET["num1"])
    res = num1 * 4 * 1 / 100
    num2 = num1
    res1 = round(num2 / 0.7 - 5, 2)
    num3 = num1
    res2 = round(num3 / 1.09, 2)
    num4 = num1
    res3 = round(num4 / 18 - 0.1, 2)
    num5 = num1
    res4 = round(num5 / 0.7 + 4.4, 2)
    num6 = num1
    res5 = round(num6 / 0.8 + 3.12, 2)
    return render(request, 'murrah buffalo result.html',
                  {"Total": num1, "result": res, "result1": res1, "result2": res2, "result3": res3, "result4": res4,
                   "result5": res5})


def add5(request):
    num1 = int(request.GET["num1"])
    res = num1 * 4 * 1 / 100
    num2 = num1
    res1 = round(num2 / 0.7 - 5, 2)
    num3 = num1
    res2 = round(num3 / 1.09, 2)
    num4 = num1
    res3 = round(num4 / 18 - 0.1, 2)
    num5 = num1
    res4 = round(num5 / 0.7 + 4.4, 2)
    num6 = num1
    res5 = round(num6 / 0.8 + 3.12, 2)
    return render(request, 'bhadawari buffalo result.html',
                  {"Total": num1, "result": res, "result1": res1, "result2": res2, "result3": res3, "result4": res4,
                   "result5": res5})


def add6(request):
    num1 = int(request.GET["num1"])
    res = num1 * 4 * 1 / 100
    num2 = num1
    res1 = round(num2 / 0.7 - 5, 2)
    num3 = num1
    res2 = round(num3 / 1.09, 2)
    num4 = num1
    res3 = round(num4 / 18 - 0.1, 2)
    num5 = num1
    res4 = round(num5 / 0.7 + 4.4, 2)
    num6 = num1
    res5 = round(num6 / 0.8 + 3.12, 2)
    return render(request, 'pandharpuri buffalo result.html',
                  {"Total": num1, "result": res, "result1": res1, "result2": res2, "result3": res3, "result4": res4,
                   "result5": res5})


def add7(request):
    num1 = int(request.GET["num1"])
    res = num1 * 4 * 1 / 100
    num2 = num1
    res1 = round(num2 / 0.7 - 5, 2)
    num3 = num1
    res2 = round(num3 / 1.09, 2)
    num4 = num1
    res3 = round(num4 / 18 - 0.1, 2)
    num5 = num1
    res4 = round(num5 / 0.7 + 4.4, 2)
    num6 = num1
    res5 = round(num6 / 0.8 + 3.12, 2)
    return render(request, 'nagpuri buffalo result.html',
                  {"Total": num1, "result": res, "result1": res1, "result2": res2, "result3": res3, "result4": res4,
                   "result5": res5})
