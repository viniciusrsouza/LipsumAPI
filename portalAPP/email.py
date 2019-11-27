from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_link(email, token):
    subject = 'Link para cadastro no grupo TAG'
    message = 'Link para cadastro: ' + '127.0.0.1:3000/register/' + token
    from_email = 'lipsumbcc@gmail.com'
    send_mail(subject,message,from_email,[email],fail_silently=False)

'''
def send_email(self, email, customer_name, email_language='en_US'):


    html_content = render_to_string('email.html', {'email': email, 'actionurl': url,
                                                        'customer_name': customer_name})  # render with dynamic value



    return msg.send()
'''