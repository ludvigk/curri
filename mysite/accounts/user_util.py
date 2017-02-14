from django.contrib.auth.models import User


def username_present(username):
    if User.objects.filter(username=username).exists():
        return True
    return False


def email_present(email):
    if User.objects.filter(email=email).exists():
        return True

    return False
