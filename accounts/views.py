from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request , 'register.html',
                        {'form' : form}
    )
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data = request.POST)
        if form.is_valid():
            print("LOGIN SUCCESS")
            user = form.get_user()

            login(request, user)

            return redirect('/')

        else:

            print("LOGIN FAILED")
            print(form.errors)
    else:
        form = AuthenticationForm()        

    return render(
        request , 'login.html' , {'form':form}
    )

def user_logout(request):
    logout(request)
    return redirect("/")