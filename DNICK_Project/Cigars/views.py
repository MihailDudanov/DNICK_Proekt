from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def pocetna(request):
    cigars=Proizvod.objects.filter().all()
    kupuvaci=Kupuvac.objects.filter().all()
    prodavaci=Prodavac.objects.filter().all()
    context={"cigars": cigars, "kupuvaci" : kupuvaci , "prodavaci" : prodavaci }
    return render(request,"pocetna.html",context=context)

def za_nas(request):
    cigars=Proizvod.objects.filter().all()
    kupuvac=Kupuvac.objects.filter().all()
    prodavac=Prodavac.objects.filter().all()
    context={"cigars": cigars, "kupuvac" : kupuvac , "prodavac" : prodavac }
    return render(request,"za_nas.html",context=context)

def cigars(request):

    cigars=Proizvod.objects.all()
    context={"cigars":cigars, "form":ProizvodForm}
    return render(request,"cigars.html",context=context)

def prodavac(request):
    if request.method == "POST":
        form_data=ProdavacForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            ProdavacForm.user=form_data.save(commit=False)
            ProdavacForm.user=request.user
            ProdavacForm.user.save("prodavac")

    context={"prodavac":prodavac, "form":ProdavacForm}
    return render(request,"prodavac.html",context=context)

def kupuvac(request):
    if request.method == "POST":
        form_data=KupuvacForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            KupuvacForm.user=form_data.save(commit=False)
            KupuvacForm.user=request.user
            KupuvacForm.user.save("kupuvac")

    context={"kupuvac":kupuvac, "form":KupuvacForm}
    return render(request,"kupuvac.html",context=context)

def naracka(request, id=0):
    naracka = Proizvod.get(id)
    context = {"naracka": naracka()}
    return render(request, "proizvod.html", context=context)

def najava(request):
    korisnik=Najava.objects.filter().all()
    context = {"korisnik": korisnik,}
    return render(request, "najava.html", context=context)


