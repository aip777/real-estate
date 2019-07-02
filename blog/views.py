from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

from .models import blog

from django.http import HttpResponse

def blogview(request):
    blog_obj = blog.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(blog_obj, 6)
    page = request.GET.get('page')


    paged_listings = paginator.get_page(page)
    context = {
        'blog_new' : paged_listings
    }

    return render(request,  'blog/blog.html', context,)


def blogid(request, blog_id ):

    blog_object = get_object_or_404(blog, pk = blog_id)

    context = {
        'blog_object': blog_object
    }

    return render(request, 'blog/blogid.html', context)