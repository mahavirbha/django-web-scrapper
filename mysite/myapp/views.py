from django.shortcuts import render
from .models import Link
from django.conf import settings
import subprocess
from django.http import HttpResponse
import os


# Create your views here.

def scrape(request):
    # page = requests.get("https://youtube.com/")
    # soup = BeautifulSoup(page.text, 'html.parser')

    # # print("soup:", soup)

    # for link in soup.find_all('a'):
    #     link_address = link.get('href')
    #     link_text = link.string
    #     Link.objects.create(address=link_address, name=link_text)
    script_path = os.path.join(settings.SCRIPTS_DIR, 'bsexemple.py')
    result = subprocess.run(['python', script_path], capture_output=True)

    code = "from scripts.bsexemple import bsscript; text, adr = bsscript()"
    exec(code, globals())

    for i in range(len(adr)):
        Link.objects.create(address=adr[i], name=text[i])

    data = Link.objects.all()

    return render(request, 'myapp/result.html', {'data': data})
    # return HttpResponse()
