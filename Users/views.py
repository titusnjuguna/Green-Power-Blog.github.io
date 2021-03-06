from django.shortcuts import render,redirect
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method =='POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            form.data_cleaned.get('username')
            messages.success(request,"Account created successfully, kindly login")
            return redirect('Login')
    else:
        form = UserRegisterForm()
    return render(request, 'Users/register.html',{'form':form})
@login_required
def Profile(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated successful ')
            return redirect('Profile')
    else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            context = {
                        'u_form': u_form,
                        'p_form': p_form
                    }
    return render(request,'Users/profile.html', context)






