import email
from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render, redirect
import json
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from robbob import settings
from django.views.decorators.csrf import csrf_exempt
from .models import *
import requests
from robbob import settings

def home(request):
    services = Uslugi.objects.all()
    opinions = Opinie.objects.all()
    photos = Realizacje.objects.all()
    edit = Edycje.objects.first()
    context = {'services':services, 'opinions':opinions, 'photos':photos, 'range': range(1,6), 'edit':edit}
    return render(request, 'main/home.html', context)

@csrf_exempt

def contact(request):
    data = json.loads(request.body)

    captcha_token=data['form']['token']
    captcha_url="https://www.google.com/recaptcha/api/siteverify"
    captcha_secret=settings.GOOGLE_RECAPTCHA_SECRET_KEY
    captcha_data={"secret":captcha_secret,"response":captcha_token}
    captcha_server_response=requests.post(url=captcha_url, data=captcha_data)
    captcha_json=json.loads(captcha_server_response.text)

    if captcha_json['success']==False:
        return JsonResponse('error', safe=False)
    else:
        temat="Nowa wiadomość - " + data['form']['name']
        html_content = render_to_string("main/nowa_wiadomosc.html", {'data':data['form']})
        text_content = strip_tags(html_content)
        emaill = EmailMultiAlternatives(
            #temat  
            temat,
            #tresc
            text_content,
            #od
            settings.EMAIL_HOST_USER,
            #do
            ['szymon.kalkowski@wp.pl', 'foxsentertainmentgroup@gmail.com']
        )
        emaill.attach_alternative(html_content, "text/html")
        emaill.send()

        temat2="Dziękujemy za wiadomość - Foxtry"
        html_content2 = render_to_string("main/dziekujemy_wiadomosc.html", {'data': data['form']})
        text_content2 = strip_tags(html_content2)
        emaill2 = EmailMultiAlternatives(
            #temat
            temat2,
            #tresc
            text_content2,
            #od
            settings.EMAIL_HOST_USER,
            #do
            [data['form']['email']]
        )
        emaill2.attach_alternative(html_content2, "text/html")
        emaill2.send()

        return JsonResponse('success', safe=False)


@csrf_exempt

def opinion(request):
    data = json.loads(request.body)

    captcha_token=data['form']['token']
    captcha_url="https://www.google.com/recaptcha/api/siteverify"
    captcha_secret=settings.GOOGLE_RECAPTCHA_SECRET_KEY
    captcha_data={"secret":captcha_secret,"response":captcha_token}
    captcha_server_response=requests.post(url=captcha_url, data=captcha_data)
    captcha_json=json.loads(captcha_server_response.text)

    if captcha_json['success']==False:
        return JsonResponse('error', safe=False)
    else:
        x = Opinie(imie=data['form']['name'], email=data['form']['email'], ocena=int(data['form']['rating']), opinia=data['form']['opinion'])
        x.save()
        return JsonResponse('success', safe=False)

