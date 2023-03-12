from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Profile

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles": profiles})
    else:
        messages.success(request, ("Voce precisa estar logado para ver!"))
        return redirect('home')