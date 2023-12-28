from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile

@login_required
def profile(request):
    return render(request, 'userprofile/profile.html', {'user': request.user})

def edit_profile(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save(request.user)
            return redirect('/userprofile/profile/')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'userprofile/editprofile.html', {'form': form, 'user': request.user})

