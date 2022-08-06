from django.shortcuts import redirect, render
from .forms import ContactForm

# Create your views here.
def contact_page(request):
    return render(request, 'contact/contact.html')

def appointment(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        print(form.errors)
        return redirect('contact-page')
    else:
        return redirect('contact-page')   