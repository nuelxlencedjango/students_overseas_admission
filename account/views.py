
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from .forms import *
from django.shortcuts import redirect
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def registration(request):
    error = ''
    #if request.user.is_authenticated:

       # return HttpResponseRedirect(reverse('account:p_dashboard'))

    form = SignUpForm()
    form2 = AgentsForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = AgentsForm(request.POST, request.FILES)
        print(form.errors)
        print(form2.errors)
        
        if form.is_valid() and form2.is_valid():
            user = form.save()
            partner = form2.save(commit=False)
            partner.user = user
            partner.save()

            #user.save()         
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
      
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'success')
                
                return HttpResponseRedirect(reverse('core_app:home'))

            return HttpResponseRedirect(reverse('account:register_page'))

        else:
            if User.objects.filter(username=request.POST['username']).exists():
                error = 'A customer with this username already exists'

            else:
                error = 'Your password is not strong enough or both password must be same'
        

    return render(request, 'account/register.html', context={'form': form, 'form2':form2,  'user': "Customer Register", 'error': error})





def loginPage(request):
    form = PartnersLoginForm()
    if request.method == 'POST':
        form = PartnersLoginForm(data=request.POST)
      
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('account:p_dashboard'))

        else:
            return render(request, 'account/login.html', context={'form': form, 'user': "Customer Login", 'error': 'Invalid username or password'})
    return render(request, 'account/login.html', context={'form': form, 'user': "Customer Login"})





@login_required()
def logoutPage(request):
    logout(request)
    return redirect('core_app:home')





@login_required
def dashboard(request):
    user = request.user
    return render(request, 'base2/index.html')


