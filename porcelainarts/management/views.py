from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.http import HttpResponse
from .forms import *
from .models import Inventari, Furnizimi, Shitje
from porcelainart.models import *
from django.db.models import Sum
from django.contrib.auth import authenticate,  login, logout
from forms import UserLoginForm
import csv
from django.http import JsonResponse



def index(request):
    products = Inventari.objects.filter(gjendje__lte=3)
    context = {'products': products, }
    return render(request, 'inventory/index.html', context)

def inventari(request):
    products = Inventari.objects.all()
    context = {'products': products, }
    return render(request, 'inventory/inventari.html', context)


def detail(request, pk):
    product = get_object_or_404(Inventari, pk=pk)
    return render(request, 'inventory/detail.html', {'product': product})


def addnew(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()

            # product = Product()
            # product.name = form.cleaned_data['name']
            # product.cetagory = form.cleaned_data['cetagory']
            # product.supplier = form.cleaned_data['supplier']
            # product.unit_price = form.cleaned_data['unit_price']
            # product.description = form.cleaned_data['description']
            # product.save()
            # return redirect('detail', pk=product.pk)
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'inventory/new.html', {'form': form})


def edit(request, pk):
    product = get_object_or_404(Inventari, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/edit.html', {'form': form})


#furnizim
def furnizimi(request):
    furnizim = Furnizimi.objects.all()
    context = {'furnizim': furnizim}
    return render(request, 'inventory/furnizim.html', context)


def addnewFurnziim(request):
    if request.method == 'POST':
        form = FurnizimForm(request.POST)

        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()

            # product = Product()
            # product.name = form.cleaned_data['name']
            # product.cetagory = form.cleaned_data['cetagory']
            # product.supplier = form.cleaned_data['supplier']
            # product.unit_price = form.cleaned_data['unit_price']
            # product.description = form.cleaned_data['description']
            # product.save()
            # return redirect('detail', pk=product.pk)
            return redirect('furnizimi')
    else:
        form = FurnizimForm()
    return render(request, 'inventory/new.html', {'form': form, })


def detailFurnizim(request, pk):
    furnizim = get_object_or_404(Furnizimi, pk=pk)
    return render(request, 'inventory/detailFurnizime.html', {'furnizim': furnizim})


def editFurnizim(request, pk):
    furn = get_object_or_404(Furnizimi, pk=pk)
    if request.method == "POST":
        form = FurnizimForm(request.POST, instance=furn)
        if form.is_valid():
            form.save()
            return redirect('furnizimi')
    else:
        form = FurnizimForm(instance=furn)
    return render(request, 'inventory/editFurnizim.html', {'form': form})


#shitje
def shitje(request):
    shitjet = Shitje.objects.all()
    context = {'shitjet': shitjet, }
    return render(request, 'inventory/shitje.html', context)


def addnewShitje(request):
    if request.method == 'POST':
        form = ShitjeForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()

            # product = Product()
            # product.name = form.cleaned_data['name']
            # product.cetagory = form.cleaned_data['cetagory']
            # product.supplier = form.cleaned_data['supplier']
            # product.unit_price = form.cleaned_data['unit_price']
            # product.description = form.cleaned_data['description']
            # product.save()
            # return redirect('detail', pk=product.pk)
            return redirect('shitje')
    else:
        form = ShitjeForm()
    return render(request, 'inventory/new.html', {'form': form})

def detailShitje(request, pk):
    shitjet = get_object_or_404(Shitje, pk=pk)
    return render(request, 'inventory/detailShitje.html', {'shitjet': shitjet})


def editShitje(request, pk):
    shit = get_object_or_404(Shitje, pk=pk)
    if request.method == "POST":
        form = ShitjeForm(request.POST, instance=shit)
        if form.is_valid():
            form.save()
            return redirect('shitje')
    else:
        form = ShitjeForm(instance=shit)
    return render(request, 'inventory/editShitje.html', {'form': form})


#klienti
def klienti(request):
    klient = Klienti.objects.all()
    context = {'klient': klient, }
    return render(request, 'inventory/klient.html', context)


def addnewKlienti(request):
    if request.method == 'POST':
        form = KlientiForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()

            # product = Product()
            # product.name = form.cleaned_data['name']
            # product.cetagory = form.cleaned_data['cetagory']
            # product.supplier = form.cleaned_data['supplier']
            # product.unit_price = form.cleaned_data['unit_price']
            # product.description = form.cleaned_data['description']
            # product.save()
            # return redirect('detail', pk=product.pk)
            return redirect('klienti')
    else:
        form = KlientiForm()
    return render(request, 'inventory/new.html', {'form': form})


def detailKlient(request, pk):
    klient = get_object_or_404(Klienti, pk=pk)
    return render(request, 'inventory/detailKlienti.html', {'klient': klient})


def editKlient(request, pk):
    kli = get_object_or_404(Klienti, pk=pk)
    if request.method == "POST":
        form = KlientiForm(request.POST, instance=kli)
        if form.is_valid():
            form.save()
            return redirect('klienti')
    else:
        form = KlientiForm(instance=kli)
    return render(request, 'inventory/editKlient.html', {'form': form})

#produktet nga faqa web
def produktet_web(request):
    produktet = Product.objects.all()
    context = {'produktet': produktet, }
    return render(request, 'inventory/produktet.html', context)
def detailProdukt(request, pk):
    produkti = get_object_or_404(Product, pk=pk)
    return render(request, 'inventory/detailProduktet.html', {'produkti': produkti})
def addnewProdukt(request):
    if request.method == 'POST':
        form = ProduktForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()

            # product = Product()
            # product.name = form.cleaned_data['name']
            # product.cetagory = form.cleaned_data['cetagory']
            # product.supplier = form.cleaned_data['supplier']
            # product.unit_price = form.cleaned_data['unit_price']
            # product.description = form.cleaned_data['description']
            # product.save()
            # return redirect('detail', pk=product.pk)
            return redirect('produktet')
    else:
        form = ProduktForm()
    return render(request, 'inventory/new.html', {'form': form})


def editProdukt(request, pk):
    produ = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProduktForm(request.POST, instance=produ)
        if form.is_valid():
            form.save()
            return redirect('produktet')
    else:
        form = ProduktForm(instance=produ)
    return render(request, 'inventory/editProdukt.html', {'form': form})

#categorite nga faqa web
def categorite_web(request):
    categorite = Category.objects.all()
    context = {'categorite': categorite, }
    return render(request, 'inventory/Kategorite.html', context)
def detailCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'inventory/detailCategory.html', {'category': category})
def addnewCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        print(dir(form))
        if form.is_valid():
            # product = form.save(commit=True)
            form.save()

            # product = Product()
            # product.name = form.cleaned_data['name']
            # product.cetagory = form.cleaned_data['cetagory']
            # product.supplier = form.cleaned_data['supplier']
            # product.unit_price = form.cleaned_data['unit_price']
            # product.description = form.cleaned_data['description']
            # product.save()
            # return redirect('detail', pk=product.pk)
            return redirect('kategorite')
    else:
        form = CategoryForm()
    return render(request, 'inventory/new.html', {'form': form})


def editCategory(request, pk):
    categ = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=categ)
        if form.is_valid():
            form.save()
            return redirect('kategorite')
    else:
        form = CategoryForm(instance=categ)
    return render(request, 'inventory/editProdukt.html', {'form': form})



def LoginView(request):
    print (request.user.is_authenticated())
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print (request.user.is_authenticated())
        return redirect("/management/index/")

    return render(request, "inventory/login.html", {"form": form})

def LogoutView(request):
    logout(request)
    print (request.user.is_authenticated())
    return redirect("/management/login/")
    return render(request, 'inventory/login.html', {})

def export_inventari_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Inventari.csv"'

    writer = csv.writer(response)
    writer.writerow(['kodiI', 'gjendje', 'cmimi_per_njesi', 'cmimi_shitjes', 'pershkrim', 'permasat'])

    produktet_csv = Inventari.objects.all().values_list('kodiI', 'gjendje', 'cmimi_per_njesi', 'cmimi_shitjes', 'pershkrim', 'permasat')
    for produkt_csv in produktet_csv:
        writer.writerow(produkt_csv)

    return response

def export_klientet_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Klientet.csv"'

    writer = csv.writer(response)
    writer.writerow(['emer', 'mbiemer', 'nrTel', 'email'])

    klientet_csv = Klienti.objects.all().values_list('emer', 'mbiemer', 'nrTel', 'email')
    for klient_csv in klientet_csv:
        writer.writerow(klient_csv)

    return response

def export_shitjet_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Shtijet.csv"'

    writer = csv.writer(response)
    writer.writerow(['kodiS', 'sasia', 'ulje', 'cmimi_per_njesi', 'cmimi_shitjes','pershkrim', 'klienti', 'kapari','data_porosise' ,'data_dorezimit'])

    shitjet_csv = Shitje.objects.all().values_list('kodiS', 'sasia', 'ulje', 'cmimi_per_njesi', 'cmimi_shitjes','pershkrim', 'klienti', 'kapari','data_porosise' ,'data_dorezimit')
    for shitje_csv in shitjet_csv:
        writer.writerow(shitje_csv)

    return response

def export_furnizim_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Furnizimet.csv"'

    writer = csv.writer(response)
    writer.writerow(['kodiF', 'data_porosise', 'cmimi_per_njesi', 'sasia', 'cmimi_total','pershkrim', 'permasat'])

    furnizimet_csv = Furnizimi.objects.all().values_list('kodiF', 'data_porosise', 'cmimi_per_njesi', 'sasia', 'cmimi_total','pershkrim', 'permasat')
    for furnizim_csv in furnizimet_csv:
        writer.writerow(furnizim_csv)

    return response

def export_perFurnizim_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Per furnizim.csv"'

    writer = csv.writer(response)
    writer.writerow(['kodiI', 'gjendje', 'cmimi_per_njesi', 'cmimi_shitjes', 'pershkrim', 'permasat'])

    perfurnizimet_csv = Inventari.objects.filter(gjendje__lte=3).values_list('kodiI', 'gjendje', 'cmimi_per_njesi', 'cmimi_shitjes', 'pershkrim', 'permasat')
    for perfurnizim_csv in perfurnizimet_csv:
        writer.writerow(perfurnizim_csv)

    return response

