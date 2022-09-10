from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from blogs.forms import UserRegisterForm


def register(request):
    # Process completed form
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            # return redirect('home')  #used a global login_redirect_url
            
            #Method 2
            # form.save()
            # return redirect('login')

    else:
        # Register a new user
        form = UserRegisterForm()

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
