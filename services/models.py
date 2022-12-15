from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class Job(models.Model):
    """Model representing a job (but not a specific job)."""
    title = models.CharField(max_length=200)

    description = models.TextField(max_length=1000, help_text='Enter a brief description of the job')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this job."""
        return reverse('job-detail', args=[str(self.id)])


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this form."""
        return reverse('form-detail', args=[str(self.id)])

