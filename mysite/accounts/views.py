from . import user_util
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core import validators
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import Context, loader
import random
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def login(request):
    username = request.POST.get('loginusername', '')
    password = request.POST.get('loginpassword', '')
    user = authenticate(username=username, password=password)
    if user is not None or request.user.is_authenticated():
        auth_login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html')


def register(request):
    try:
        p = request.GET.copy()
        username = p.get('username', '')
        email = p.get('email', '')
        password = p.get('password', '')
        assert(user_util.username_valid(username))
        assert(user_util.email_valid(email))
        user = User.objects.create_user(username, email, password)
        user.is_active = False
        user.save()
        try:
            send_registration_confirmation(user)
        except Exception as e:
            user.delete()
            return HttpResponse(False)
    except Exception as e:
        return HttpResponse(False)
    return HttpResponse(True)


def send_registration_confirmation(user):
    from django.utils.http import urlsafe_base64_encode
    from django.utils.encoding import force_bytes
    from . import mailer
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    title = "Curri email verification"
    mail = mailer.Mailer()
    mail.send_messages(subject=title, template='accounts/verification_email.html',
                       context={'protocol': 'http', 'domain': 'localhost', 'token': token,
                                'uid': uid},
                       to_emails=[user.email])


def activationview(request, uidb64, token):
    if uidb64 is not None and token is not None:
        from django.utils.http import urlsafe_base64_decode
        uid = urlsafe_base64_decode(bytes(uidb64, encoding='UTF-8'))
        try:
            from django.contrib.auth import get_user_model
            from django.contrib.auth.tokens import default_token_generator
            user_model = get_user_model()
            user = user_model.objects.get(pk=uid.decode('UTF-8'))
            if default_token_generator.check_token(user, token) and not user.is_active:
                user.is_active = True
                auth_login(request, user)
                user.save()
                return render(request, 'accounts/verification_successful.html')
        except Exception as e:
            return render(request, 'accounts/verification_failed.html')
    return render(request, 'accounts/verification_failed.html')


def checkusername(request):
    if request.method == "GET":
        p = request.GET.copy()
        if 'username' in p.keys():
            name = p['username']
            return HttpResponse(user_util.username_valid(name))
    return HttpResponse('Invalid request')


def checkemail(request):
    if request.method == "GET":
        p = request.GET.copy()
        if 'email' in p.keys():
            email = p['email']
            return HttpResponse(user_util.email_valid(email))
    return HttpResponse('Invalid request')


def change_password(request):
    return HttpResponse(request.method)
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        update_session_auth_hash(request, form.user)
    else:
        form = PasswordChangeForm(user=request.user)
        update_session_auth_hash(request, form.user)
    return redirect('login')
