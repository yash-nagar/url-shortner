from django.shortcuts import render
import requests
from url_shorter.forms import ShortenerForm
import json


def home_view(request):
    template = 'url_shorter/home.html'
    context = dict()
    context['form'] = ShortenerForm()
    if request.method == 'GET':
        return render(request, template, context)
    elif request.method == 'POST':
        url = 'http://localhost:8000/api/data/'
        r = requests.post(url, json={"long_url": request.POST.get('long_url')})
        response_data = json.loads(r.content)
        context['new_url'] = response_data.get('short_url')
        context['long_url'] = request.POST.get('long_url')
        return render(request, template, context)
