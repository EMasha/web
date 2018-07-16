from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from forms import *
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from email.mime.image import MIMEImage
from django.template.loader import get_template
from django.core.files.uploadedfile import SimpleUploadedFile



# Create your views here.
def home (request):
    a = Product.objects.all()
    return render(request,'porcelainarts/Products/home.html',{'a': a})


def product_list(request, category_slug=None, subcategory_slug=None):
    category = None
    subcategory = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'porcelainarts/Products/list.html', {'category':category,'categories':categories,  'products':products, 'page': page })

def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = id
    return render(request, 'porcelainarts/Products/detail.html',{'product':product, 'categories':categories, 'cart_product_form':cart_product_form})

def product_query (request):
    if request.method == 'GET':
        queryset_list = Product.objects.all()
        query = request.GET.get("search", None)
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)
            )
        paginator = Paginator(queryset_list, 10)
        page = request.GET.get('page')
        try:
            queryset_list = paginator.page(page)
        except PageNotAnInteger:
            queryset_list = paginator.page(1)
        except EmptyPage:
            queryset_list = paginator.page(paginator.num_pages)


    return render(request,'porcelainarts/Products/search-results.html',{'queryset_list': queryset_list, 'page':page})

def contact(request):
    categories = Category.objects.all()
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            subject = request.POST.get('subject', '')
            from_email = request.POST.get('from_email', '')
            message = request.POST.get('message', '')
            contact_number = request.POST.get('contact_number', '')

            # Email the profile with the
            # contact information
            template = get_template('porcelainarts/Products/contact_template.txt')
            context = {'subject': subject,'from_email': from_email,'message': message, 'contact_number':contact_number}
            content = template.render(context)

            admin_email = settings.EMAIL_HOST_USER
            email = EmailMessage(
                "Porosi e re",
                content,
                "Your website" +'',
                [admin_email],
                headers = {'Reply-To': from_email }

            )
            email.attach(filename='foto1.jpg', content='attachment.read()', mimetype='image/jpeg')
            email.send()
            return redirect('/success')
        else:
            return redirect('/error')

    return render(request, 'porcelainarts/Products/contact.html', {'categories':categories,'form': form_class})

def successView(request):
    return render(request, 'porcelainarts/Products/success.html')
def errorView(request):
    return render(request, 'porcelainarts/Products/fail.html')
