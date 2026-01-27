from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm
from django.views.decorators.csrf import csrf_exempt


def signup_view(request):
    if request.method == 'POST':
        print("POST DATA:", request.POST)  # 🔥 DEBUG LINE

        form = SignupForm(request.POST)
        if form.is_valid():
            print("FORM IS VALID")  # 🔥 DEBUG LINE

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            print("USER SAVED:", user.cnic)  # 🔥 DEBUG LINE
            return redirect('login')
        else:
            print("FORM ERRORS:", form.errors)  # 🔥 DEBUG LINE

    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


from django.contrib.auth import authenticate, login

from django.contrib import messages
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        cnic = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=cnic, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "You have entered wrong CNIC or password")

    return render(request, 'accounts/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')
