from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):

    if request.method == "POST":
        message_name = request.POST["message-name"]
        message_email = request.POST["message-email"]
        message = request.POST["message"]

        #send an Email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from Email
            ["akellerdesign@zohomail.eu"], # To Email
            fail_silently=False,
        )

        return render(request, "contact.html", {"message_name" : message_name})
    else:
        return render(request, "contact.html", {})
