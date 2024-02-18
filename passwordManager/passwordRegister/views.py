import csv

from django.shortcuts import render,redirect
from .forms import PasswordForm
from .models import Website
from django.http import HttpResponse
from .forms import CSVImportForm
import csv

# Les vues.

def password_list(request):
    context = {'password_list': Website.objects.all()}
    return render(request, 'passwordRegister/password_list.html',context)

def password_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = PasswordForm()
        else:
            website = Website.objects.get(pk=id)
            form = PasswordForm(instance=website)
        return render(request, 'passwordRegister/password_form.html', {'form': form})
    else:
        if id == 0:
            form = PasswordForm(request.POST)
        else:
            website = Website.objects.get(pk=id)
            form = PasswordForm(request.POST,instance=website)
        if form.is_valid():
            form.save()
        return redirect('/')

def password_delete(request,id):
    website = Website.objects.get(pk=id)
    website.delete()
    return redirect('/')

def password_export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['name', 'url', 'username', 'password'])

    for website in Website.objects.all().values_list('name', 'url', 'username', 'password'):
        writer.writerow(website)

    response['Content-Disposition'] = 'attachment; filename="passwords.csv"'

    return response

def password_import(request):
    ## Pas de résultats concluant
        