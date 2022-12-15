from django.forms import ModelForm
from .models import Contact

# form for the contact page


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

