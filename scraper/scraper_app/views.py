from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import Link

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')
        if site:  
            page = requests.get(site)
            soup = BeautifulSoup(page.text, 'html.parser')

            for link in soup.find_all('a'):
                link_address = link.get('href')
                link_text = link.string
                if link_address:  
                    Link.objects.create(address=link_address, name=link_text)
    

    data = Link.objects.all()
    return render(request, 'result.html', {'data': data})

def clear(request):
    Link.objects.all().delete()
    return redirect('/') 