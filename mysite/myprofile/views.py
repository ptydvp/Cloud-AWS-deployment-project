from django.shortcuts import render, redirect
from .forms import UserUpdateForm, ProfileUpdateForm

# Create your views here.
def profile(request):
    if request.method == 'POST':
        userform = UserUpdateForm(request.POST, instance=request.user)
        profileform = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('Profile')

    else:
        userform = UserUpdateForm(instance=request.user)
        profileform = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'userform': userform,
        'profileform': profileform
    }

    return render(request, 'myprofile/profile.html', context)