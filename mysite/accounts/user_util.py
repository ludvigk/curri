from django.contrib.auth.models import User
from django.core import validators
import re


def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    return False


def email_present(email):
    if User.objects.filter(email=email).exists():
        return True
    return False


def username_valid(username):
    if username_present(username) or username == '':
        return False
    if len(username) < 4 or len(username) > 20:
        return False
    if not re.match("[a-zA-Z0-9]*", username):
        return False
    return True


def email_valid(email):
    if email_present(email):
        return False
    try:
        validators.validate_email(email)
    except Exception:
        return(False)
    return True
