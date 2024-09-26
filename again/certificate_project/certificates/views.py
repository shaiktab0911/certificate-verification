from django.shortcuts import redirect, render
from pymongo import MongoClient
import os

client = MongoClient('mongodb://localhost:27017/')
db = client['certificate_db']
certificates_collection = db['certificates']

def home(request):
    return redirect('get_certificate')


def get_certificate(request):
    certificate = None
    if 'certificate_id' in request.GET:
        certificate_id = request.GET['certificate_id']
        certificate = certificates_collection.find_one({'certificate_id': certificate_id})
        if certificate:
            certificate['image_path'] = os.path.join('/static/certificates/', os.path.basename(certificate['image_path']))
    return render(request, 'certificate_form.html', {'certificate': certificate})
