from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy, reverse

from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views import View

from .forms import BookForm
from .models import Book


class Home(TemplateView):
    template_name = 'home.html'


# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         context['url'] = fs.url(name)
#     return render(request, 'core/upload.html', context)
#
#
# def book_list(request):
#     if not request.user.email.endswith('palash@palash.com'):
#         return HttpResponse("You can't leave a review for this book.")
#
#     books = Book.objects.all()
#     return render(request, 'core/book_list.html', { 'books': books })
#
#
# def upload_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'core/upload_book.html', {
#         'form': form
#     })
#
#
# def delete_book(request, pk):
#     if request.method == 'POST':
#         book = Book.objects.get(pk=pk)
#         book.delete()
#     return redirect('book_list')


class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = '/accounts/login/'
    permission_required = "auth.change_user"

    model = Book
    template_name = 'core/class_book_list.html'
    context_object_name = 'books'




class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_upload_book')

    template_name = 'core/upload_book.html'

    # def post(self, request, *args, **kwargs):
    #     form = BookForm(request.POST)
    #     if form.is_valid():
    #         book = form.save()
    #         book.save()
    #         return HttpResponseRedirect(reverse_lazy('class_upload_book'))
    #     return render(request, 'core/upload_book.html', {'form': form})


# class DeleteBooks(DeleteView):
#     template_name = 'core/class_book_list.html'
#
#     def get_object(self):
#         id_ = self.kwargs.get(" pk ")
#         return get_object_or_404(pk = id_)
#
#     def get_success_url(self):
#         return reverse ('class_book_list')



def class_delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('class_book_list')






def contactus(request):
    form = BookForm(request.POST or None)


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



