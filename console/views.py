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

def get_recent_flows(request):
    RESPONSE = {}

    for flow in Flow.objects.all():
        RESPONSE[flow.id] = {
            'flow' : flow.flow,
            'is_cheque' : flow.is_cheque,
            'catalyst' : flow.catalyst,
            'purpose' : flow.purpose,
            'amount': flow.amount,
            'account': flow.account.id,
            'time_created': flow.time_created
        }


    return JsonResponse(RESPONSE)


def add_flow(request):
    try:
        if request.method == 'POST':
            print(request.POST)
                
            print(request.POST['flow_direction_input'])
            print(request.POST['catalyst_name'])
            print(request.POST['purpose'])
            print(request.POST['amount'])
            print(request.POST['accounts_select'])
            print('is_cheque' in request.POST)

            acc = Account.objects.get(id=request.POST['accounts_select'])

            fo =Flow.objects.create(
                flow = request.POST['flow_direction_input'].lower(),
                is_cheque = 'is_cheque' in request.POST,
                catalyst = request.POST['catalyst_name'],
                purpose = request.POST['purpose'],
                amount = request.POST['amount'],
                account = acc
            )

            fo.save()

            if fo.flow == 'deposit':
                # Add
                acc.amt_present += float(fo.amount)
                acc.save()
            else:
                # Substract
                acc.amt_present -= float(fo.amount)
                acc.save()


            # Change the account

            messages.success(request, "Added Flow successfully")

    except Exception as e:
        messages.error(request, 'Server error! Check the terminal')
        print(e)

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

    