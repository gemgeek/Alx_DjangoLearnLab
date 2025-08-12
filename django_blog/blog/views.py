from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # optional: log user in immediately
            login(request, user)
            return redirect('home')  # change to your home route name or '/'
    else:
        form = SignUpForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'blog/profile.html', context)
