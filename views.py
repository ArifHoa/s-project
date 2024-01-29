
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .regstar import CreateUserForm,LoginForm


def homepage (request):
    return render(request, 'homes.html')


def home_to_fulpag (request):
    return render(request,'home_to.html')




def reg_star (request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('sing_ins')
    context = {
        'regist':form
    }        
    return render(request, 'regstar/singup.html',context)






def sing_in(request):
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_to_fulpag')

    context = {
        'login_form': login_form
    }
    return render(request, 'regstar/singin.html', context)



def logout_fan (request):
    logout(request)
    return redirect('sing_ins')