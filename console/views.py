from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Account, Flow






# Create your views here.
@login_required(login_url='/login')
def home(request):
    PARAMS = {"active_page": "dashboard"}
    return render(request, 'home.html', PARAMS)

@login_required(login_url='/login')
def accounts(request):
    PARAMS = {"active_page": "accounts"}
    return render(request, 'accounts.html', PARAMS)

@login_required(login_url='/login')
def hoardings(request):
    PARAMS = {"active_page": "hoardings"}
    return render(request, 'hoardings.html', PARAMS)

@login_required(login_url='/login')
def customers(request):
    PARAMS = {"active_page": "customers"}
    return render(request, 'customers.html', PARAMS)

# APIs --------------------------------------------------------------

def get_accounts(request):

    RESPONSE = {}

    for account in Account.objects.all():
        RESPONSE[account.id] = {
            'name' : account.name,
            'location' : account.location,
            'amt_present' : account.amt_present,
            'category' : account.category,
            'pd_upcoming_date': account.pd_upcoming_date,
            'pd_amt': account.pd_amt
        }




    return JsonResponse(RESPONSE)

def add_flow(request):
    if request.method == 'POST':
        print(request.POST['flow_direction_input'])
        print(request.POST['catalyst_name'])
        print(request.POST['purpose'])
        print(request.POST['amount'])

    return redirect('accounts')


# Auth ---------------------------------------------------------------


def loginpage(request):
    return render(request, 'login.html')

def handle_login(request):

    print("Handle the login")

    if request.method == 'POST':
        # RESPONSE = {"SUCCESS": True, "ERRORS": []}

        print(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        # Frisk Data
        if User.objects.filter(username=username).first() == None:
            # RESPONSE['SUCCESS'] = False
            # RESPONSE['ERROR'].append("Username does not exist!")
            messages.error(request, "Username does not exist!")
            
            return redirect('login')
        
        login_user = authenticate(username=username, password=password)

        if login_user is None:
            messages.error(request, "Invalid Passsword!")
            return redirect('login')
        
        # Correct Creds - Login Now... HAYAKU!

        messages.success(request, f"Logged in as {login_user}!")

        login(request, login_user)

        return redirect('home')


def logoutuser(request):
    logout(request)
    return redirect('home')

    