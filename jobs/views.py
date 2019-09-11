from django.shortcuts import render
from .models import jobs
from faker import Faker
from django.core.exceptions import ObjectDoesNotExist
import requests
from decouple import config


# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')


def former_life(request):

    name = request.POST.get('name')
    # filter를 사용해도 된다.
    # 예시
    # job = jobs.objects.filter(name=name).first()
    # if job:
    #     pass
    # else:
    #     pass
    api_key = config('GIPHY_API_KEY')
    try:
        job = jobs.objects.get(name=name)
        url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job}&lang=ko'
        response = requests.get(url).json()
        try:
            image_url = response['data'][0].get('images').get('original').get('url')
        except IndexError:
            image_url = 'https://www.nemopan.com/files/attach/images/6294/754/394/013/90bc7f55a6b27e39e1acab9348e1b60a.gif'
        context = {
            'name': name,
            'job': job.job,
            'image_url': image_url,
        }
    except ObjectDoesNotExist:
        fake = Faker('ko_kr')
        job = fake.job()
        job_inst = jobs(name=name, job=job)
        job_inst.save()

        url = f'http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job}&lang=ko'
        response = requests.get(url).json()
        try:
            image_url = response['data'][0].get('images').get('original').get('url')
        except IndexError:
            image_url = 'https://www.nemopan.com/files/attach/images/6294/754/394/013/90bc7f55a6b27e39e1acab9348e1b60a.gif'

        context = {
            'name': name,
            'job': job,
            'image_url': image_url,
        }

    return render(request, 'jobs/former-life.html', context)