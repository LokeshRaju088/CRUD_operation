from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Candidatedirectory, Maritalstatus
from .forms import CandidateForm, CandidateUpdateForm
from django.http import HttpResponseBadRequest
import logging


def candidate_list(request):
    candidates = Candidatedirectory.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})


def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    return render(request, 'candidate_detail.html', {'candidate': candidate})


logger = logging.getLogger(__name__)


def candidate_create(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            candidate = form.save(commit=False)
            marital_status_value = form.cleaned_data['marital_status']
            marital_status_instance, created = Maritalstatus.objects.get_or_create(marital_status=marital_status_value)
            candidate.marital_status = marital_status_instance
            # Set the status field as well, similar to how you did for marital_status
            candidate.status = form.cleaned_data['status']
            candidate.save()
            print("Candidate saved successfully:", candidate.id)

            # Redirect to the candidate_detail view for the newly added candidate
            return redirect('candidate_detail', pk=candidate.id)
        else:
            logger.error("Form is not valid. Errors: %s", form.errors)
    else:
        form = CandidateForm()
    return render(request, 'candidate_form.html', {'form': form})


def candidate_update(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)

    if request.method == 'POST':
        form = CandidateUpdateForm(request.POST, instance=candidate)
        if form.is_valid():
            # Update the existing candidate object
            candidate = form.save(commit=False)

            # Update the related fields, similar to your create view
            marital_status_value = form.cleaned_data['marital_status']
            marital_status_instance, created = Maritalstatus.objects.get_or_create(marital_status=marital_status_value)
            candidate.marital_status = marital_status_instance
            candidate.status = form.cleaned_data['status']

            candidate.save()

            return redirect('candidate_list')
        else:
            logger.error("Form is not valid. Errors: %s", form.errors)
            return HttpResponseBadRequest("Invalid form data. Please check the form and try again.")
    else:
        # Use the CandidateUpdateForm with the instance of the existing candidate
        form = CandidateUpdateForm(instance=candidate)

    return render(request, 'candidate_form.html', {'form': form, 'candidate': candidate})


def candidate_delete(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    candidate.delete()
    return redirect('candidate_list')