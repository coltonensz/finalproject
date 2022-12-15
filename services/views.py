from django.shortcuts import render
from .models import Job
from django.views import generic
from .forms import ContactForm


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_job = Job.objects.all().count()

    context = {
        'num_job': num_job,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class JobListView(generic.ListView):
    model = Job


class JobDetailView(generic.DetailView):
    model = Job


def contact_view(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

