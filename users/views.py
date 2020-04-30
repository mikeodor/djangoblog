from django.shortcuts import render, redirect

from .forms import registerform, userupdateform, profileupdate
from django.contrib import messages
from django.contrib.auth.models import User


def registeruser(request):
    if request.method == 'POST':
        form = registerform(request.POST)
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exist.')

        elif form.is_valid():

            form.save()

            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            messages.info(request, f'Account created for {username}')
            return redirect('login')

    else:
        form = registerform()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
 
    return render(request, 'users/profile.html')

def update(request):
    if request.method == 'POST':
        uform = userupdateform(request.POST,instance=request.user)
        imgform = profileupdate(request.POST,request.FILES,instance=request.user.profile)

        if uform.is_valid() and imgform.is_valid():
            uform.save()
            imgform.save()
            messages.info(request,'Account Updated')
            return redirect('profile')
            


    else:
        uform = userupdateform(instance=request.user)
        imgform = profileupdate(instance=request.user.profile)

    context = {
        'uform': uform,
        'imgform': imgform
    }

    return render(request, 'users/update.html', context)
