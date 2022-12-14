from django.shortcuts import render
from .models import Job


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_job = Job.objects.all().count()

    context = {
        'num_job': num_job,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
