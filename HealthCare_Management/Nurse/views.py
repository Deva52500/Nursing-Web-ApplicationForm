from django.shortcuts import render
from .models import Nurse
from .forms import NurseForm

# Create your views here.

# adding personal details
def addDetails(request):
    if request.method == 'POST':
        form = NurseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = NurseForm()
    else:
        form = NurseForm()
    return render(request, 'nurse/job_application.html', {
        'form': form
    })

# displaying applicant details
def viewDetails(request):
    nurse = Nurse.objects.all()
    return render(request, 'nurse/home.html', {'nurse': nurse})


