from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template



def create_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    refresh['id'] = user.id
    refresh['role'] = user.role
    refresh['first_name'] = user.first_name if hasattr(user, 'first_name') else ''
    refresh['last_name'] = user.last_name if hasattr(user, 'last_name') else ''
    refresh['email'] = user.email

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
