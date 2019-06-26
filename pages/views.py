from django.shortcuts import render
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')

    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
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

    return render(request, 'pages/gallery.html')