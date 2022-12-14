from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class Job(models.Model):
    """Model representing a job (but not a specific job)."""
    title = models.CharField(max_length=200)

    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('job-detail', args=[str(self.id)])