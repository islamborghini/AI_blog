from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
def register(request):
    if request.method == 'POST':
        #Creates a form with our register data
        form = UserRegisterForm(request.POST)

        #Checks whether the data entered is valid
        if form.is_valid():
            #saves the user
            form.save()

            #gets the username and returns it in the success message in blog-home
            username = form.cleaned_data.get('username')
            messages.success(request,'Created account')
            return redirect('login')
    else:
        form = UserRegisterForm() 
    #in other case just return the form 
    return render(request, 'users/register.html', {'form': form})
