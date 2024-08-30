from django.shortcuts import render, redirect, get_object_or_404
from .models import Feline, MedicalRecord
from .forms import CatIDSearchForm
from .forms import FelineForm
import os
import paramiko
from django.conf import settings


def home_view(request):
   records = Feline.objects.all()
 #  return render(request, 'home.html', {'records': records})
   if request.user.is_authenticated:
       return render(request, 'home2.html', {'records': records})
   else:
       return render(request, 'home.html', {'records': records})
def cat_detail_view(request, feline_id):
    cat = get_object_or_404(Feline, pk=feline_id)
#    medical_records = MedicalRecord.medical_records.all()
    medical_records = MedicalRecord.objects.filter(feline=cat)
    return render(request, 'cat_detail.html', {'cat': cat, 'medical_records': medical_records})

def medical_record_search_view(request):
    form = CatIDSearchForm(request.GET or None)
    results = []
    if form.is_valid():
        name = form.cleaned_data['name']
        #feline_id = form.cleaned_data['feline_id']
        #results = MedicalRecord.objects.filter(feline_id=feline_id)
        felines = Feline.objects.filter(name__icontains=name)
        results = MedicalRecord.objects.filter(feline__in=felines)  
    return render(request, 'medical_record_search.html', {'form': form, 'results': results})

def upload_feline(request):
    if request.method == 'POST':
        form = FelineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')  # Create a success page or redirect to a relevant page
    else:
        form = FelineForm()
    return render(request, 'upload_feline.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')
