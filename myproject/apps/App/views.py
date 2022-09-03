from django.shortcuts import render
from .forms import CandidateForm
from .models import Candidate
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Login required to access private pages.
from django.views.decorators.cache import cache_control # Detroy the section after log out

# ------------------------- FRONTEND ------------------------!
# Home
def home(request):
    return render(request, 'home.html')

# Candidate registration
def register(request):
    if request.method == "POST":
        form = CandidateForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Form sent Successfully !")
            return HttpResponseRedirect('/')
        else:
            return render(request, "register.html", {'form': form})
    else:
        form = CandidateForm()
        return render(request, "register.html", {'form':form})

# ------------------------- BACKEND ------------------------!
# HR - Home page (backend)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    context = {'data_read': Candidate.objects.all()}
    return render(request, "App/backend.html", context)

# Access candidates (individually)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate(request, id):
    data = Candidate.objects.get(pk=id)
    form = Candidate(instance = data)
    context = {'form': form}
    return render(request, 'registration/login.html', context)