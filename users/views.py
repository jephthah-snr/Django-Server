from django.http.response import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
# from .forms import userregister,userupdateform,profileupdateform,upload_resume,login_form
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from . forms import login_form

def sign_up(request):
    if request.method == 'POST':
        form =  userregister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form =  userregister()
        
    return render(request, 'main/auth-login.html', {'form':form})

    
def sign_in(request):
    form = login_form(request=request, data=request.POST)
    if request.method == 'POST':
        form = login_form(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, _(f"You are now logged in as {user.username}"))
                return redirect('dashboard')
        else:
            messages.info(request, _(f"Sorry try again, seems that didnt work"))
            return redirect('sign_in')
    else:
        form = login_form()
    return render(request = request,template_name = "main/signin.html", context={"form":form})


@login_required
def user(request):
    if request.method == 'POST':
        r_form = upload_resume(request.POST, request.FILES, instance=request.user.profile)
        if r_form.is_valid():
            r_form.save()
            messages.success(request, f'your resume has been uploaded')
            return redirect('user')
    else:
        r_form = upload_resume(instance=request.user)

    context = {
        'r_form': r_form
    }
    return render(request, 'users/user.html', context)


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'users/profile_detail.html', {'user': user})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = userupdateform(request.POST, instance=request.user)
        p_form = profileupdateform(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'profile edited')
        else:
            messages.error(request, f'Error updating your profile')
        return redirect('user')
    else:
        u_form = userupdateform(instance=request.user)
        p_form = profileupdateform(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile_edit.html',context)