from django.shortcuts import render, redirect
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from realtors.models import Realtor
from icontent.models import Content
from profileband.models import Profileband
from .models import Gallery
from .forms import EmailCreateForm


from django.core.files.storage import FileSystemStorage



def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    mvp_content = Content.objects.all().filter(is_published=True)
    profileband = Profileband.objects.all().filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')






    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'mvp_content': mvp_content,
        'profileband': profileband,

    }


    return render(request, 'pages/index.html' , context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }


    return render(request, 'pages/about.html', context)


def gallery(request):
    gallery_video = Profileband.objects.all().filter(is_published=True)
    gallery_content = Gallery.objects.all().filter(is_published=True)

    context = {

        'gallery_video': gallery_video,
        'gallery_content': gallery_content,
    }

    return render(request, 'pages/gallery.html', context)






# def gallery(request):
#
#     context = {
#
#     }
#
#     return render(request, 'pages/gallery.html', context)


def contactus(request):
    form = EmailCreateForm(request.POST or None)


    errors = None
    if form.is_valid():
        form.save()
        return redirect("/")
    if form.errors:
        errors = form.errors
    context = {
        "form": form,
    }



    return render(request, 'pages/contact-us.html', context)



# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#
#     return render(request, 'upload.html', context)
#
#
# def upload_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('#/')
#     else:
#         form = BookForm()
#     return render(request, 'upload_book.html', { 'form': form })

