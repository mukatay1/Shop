from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


def auth(request):
    form = UserCreationForm()
    login_form = AuthenticationForm()

    context = {
        'form': form,
        'login_form': login_form,
        'title': 'CampitShop - Мой аккаунт'
    }

    if request.method == 'POST':
        if request.POST.get('submit') == 'sign_up':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = authenticate(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', context)

        if request.POST.get('submit') == 'sign_in':
            login_form = AuthenticationForm(request, request.POST)

            if login_form.is_valid():
                user = authenticate(
                    request,
                    username=login_form.cleaned_data.get('username'),
                    password=login_form.cleaned_data.get('password')
                )
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('home'))
