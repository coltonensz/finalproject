from django.http import HttpResponse

from django.shortcuts import render


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'services/contact.html')
