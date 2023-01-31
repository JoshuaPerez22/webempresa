from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import  ContactForm

# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if(request.method == 'POST'):
        contact_form = ContactForm(data=request.POST)
        if(contact_form.is_valid()):
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                f"De {name} <{email}>\n\nEscribió:\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ['joshp2205@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                # Ningún error
                return redirect(reverse('contact:contact')+"?ok")
            except:
                # Algo salió mal
                return redirect(reverse('contact:contact')+'?fail')

    return render(request, "contact/contact.html", {'form': contact_form})