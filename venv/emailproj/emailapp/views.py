from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Email, LinkClick
import urllib.parse

# Create your views here.


def send_email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        body = request.POST['body']
        recipient = request.POST['recipient']
        sender = 'sweenapatel.aangan@gmail.com'

        # Embed tracking link
        encoded_url = urllib.parse.quote(f'http://127.0.0.1:8000/track_click/{recipient}/?url=YOUR_URL')
        body = body.replace('YOUR_URL', encoded_url)

        email = Email.objects.create(subject=subject, body=body, sender=sender, recipient=recipient)

        send_mail(subject, body, sender, [recipient])

        return redirect('email_sent')
    return render(request, 'send_email.html')

def track_click(request, recipient):
    url = request.GET.get('url')
    email = Email.objects.get(recipient=recipient)
    link_click, created = LinkClick.objects.get_or_create(email=email, url=url)
    link_click.click_count += 1
    link_click.save()

    return redirect(url)
