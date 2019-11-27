from django.core.mail import send_mail

def send_link(email, token):
    subject = 'Link para cadastro no grupo TAG'
    message = 'Link para cadastro: ' + token
    from_email = 'lipsumbcc@gmail.com'
    send_mail(subject,message,from_email,[email],fail_silently=False)