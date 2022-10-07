from django.shortcuts import render
from django.utils.translation import activate
from . models import AccountBalance, BitcoinBalance, BounceRate, Activity, Notification, Transaction, BtcSales, eb5 as Eb5
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def homeView(request):
    activity = Activity.objects.all()
    balance = AccountBalance.objects.all()
    bitcoinbal = BitcoinBalance.objects.all()
    bounceRate = BounceRate.objects.all()
    notification = Notification.objects.all()
    transaction = Transaction.objects.all()
    sales = BtcSales.objects.all()
    eb5 = Eb5.objects.get()


    context =  {

    'activity': activity,
    'balance': balance,
    'bitcoinbal': bitcoinbal,
    'bouncerate': bounceRate,
    'notification': notification,
    'transaction': transaction,
    'sales':sales,
    'eb5': eb5


    }

    return render(request, 'treemium/index.html', context)

@login_required
def matrices(request):

    activity = Activity.objects.all()
    balance = AccountBalance.objects.first()
    bitcoinbal = BitcoinBalance.objects.all()
    bounceRate = BounceRate.objects.all()
    transaction = Transaction.objects.all()
    sales = BtcSales.objects.all()
    user = request.user
    last_login = user.last_login




    context =  {

    'activity': activity,
    'balance': balance,
    'bitcoinbal': bitcoinbal,
    'bouncerate': bounceRate,
    'last_login': last_login,
    'user':user,



    }

    return render(request, 'treemium/accounts.html', context)


@login_required
def profileView(request):
    balance = AccountBalance.objects.all()

    context =  {
    'balance': balance,
    }

    return render(request, 'main/profile.html', context)

@login_required
def RprofileView(request):
    activity = Activity.objects.all()
    balance = AccountBalance.objects.all()
    bitcoinbal = BitcoinBalance.objects.all()
    bounceRate = BounceRate.objects.all()
    notification = Notification.objects.all()


    context =  {

    'activity': activity,
    'balance': balance,
    'bitcoinbal': bitcoinbal,
    'bouncerate': bounceRate,
    'notification': notification


    }

    return render(request, 'treemium/settings-account.html', context)


def login(request):
    return render(request, 'main/signin.html')


def reset(request):
    return render(request, 'main/auth-recover-pw.html')

def error(request):
    return render(request, 'main/auth-404.html')


def home_view(request):
    return render(request, 'main/index .html')

def about(request):
    return render(request, 'main/about.html')

# def home_view(request):
#     return render(request, '')

# def home_view(request):
#     return render(request, '')

# def home_view(request):
#     return render(request, '')

# def home_view(request):
#     return render(request, '')

def Home(request):
    return render(request, 'main/index.html')

def criteria(request):
    return render(request, 'main/criteria.html')

def services(request):
    return render(request, 'main/markets.html')

def education(request):
    return render(request, 'main/education.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def success(request):
    return render(request, 'main/success.html')

def principles(request):
    return render(request, 'main/principles.html')

def apply(request):
    if request.method == 'POST':
        # first_name = request.POST['first name']
        # last_name = request.POST['last name']
        # print(first_name)
        form = forms.ApplyForm(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            messages.success(request, f"okay {fname} {lname}, you are a few steps closer to getting your loan from us,Our loan officers would reach you via the email {email}.")
            return redirect('filled')
        else:
            print(form.errors)
            return render(request,'main/error.html')
    else:
        form = forms.ApplyForm(request.POST, use_required_attribute=False)
    return render(request, 'main/form.html', {'form':form})