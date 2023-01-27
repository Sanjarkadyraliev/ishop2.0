from django.shortcuts import render
from .models import Profile


def profile(request, user_id):
    profile = Profile.objects.get(id = user_id)
    print(profile)
    context = {'profile': profile}
    return render(request, 'clients/profile.html')
