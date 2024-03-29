from django.shortcuts import render, redirect
from .models import CsvUpload
from datetime import datetime

from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy, reverse

import datetime
from django.contrib import messages

from .forms import CsvForm
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import CsvForm
from .models import CsvUpload

# @login_required
# def index(request):
#     return render(request, 'index.html')
#
# @login_required
# def list(request):
#     members_list = Member.objects.all()
#     paginator = Paginator(members_list, 5)
#     page = request.GET.get('page')
#     try:
#         members = paginator.page(page)
#     except PageNotAnInteger:
#         members = paginator.page(1)
#     except EmptyPage:
#         members = paginator.page(paginator.num_pages)
#     return render(request, 'list.html', {'members': members})
#
# @login_required
# def create(request):
#     if request.method == 'POST':
#         member = Member(
#         firstname=request.POST['firstname'],
#         lastname=request.POST['lastname'],
#         mobile_number=request.POST['mobile_number'],
#         description=request.POST['description'],
#         date=request.POST['date'],
#         created_at=datetime.datetime.now(),
#         updated_at=datetime.datetime.now(), )
#         try:
#             member.full_clean()
#         except ValidationError as e:
#             pass
#         member.save()
#         messages.success(request, 'Member was created successfully!')
#         return redirect('/list')
#     else:
#         return render(request, 'add.html')
#
# @login_required
# def edit(request, id):
#     members = Member.objects.get(id=id)
#     context = {'members': members}
#     return render(request, 'edit.html', context)
#
# @login_required
# def update(request, id):
#     member = Member.objects.get(id=id)
#     member.firstname = request.POST['firstname']
#     member.lastname = request.POST['lastname']
#     mobile_number=request.POST['mobile_number'],
#     description=request.POST['description'],
#     date=request.POST['date'],
#     member.save()
#     messages.success(request, 'Member was updated successfully!')
#     return redirect('/list')
#
# @login_required
# def delete(request, id):
#     member = Member.objects.get(id=id)
#     member.delete()
#     messages.error(request, 'Member was deleted successfully!')
#     return redirect('/list')

# @login_required
# def fileupload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         document = Document(
#         description=request.POST['description'],
#         document=myfile.name,
#         uploaded_at=datetime.datetime.now(),)
#         document.save()
#         messages.success(request, 'Member was created successfully!')
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return redirect('fileupload')
#     else:
#         documents = Document.objects.order_by('-uploaded_at')[:3]
#         context = {'documents': documents}
#     return render(request, 'fileupload.html', context)

# @login_required
# def ajax(request):
#     if request.method == 'POST':
#         if request.is_ajax():
#             data = Ajax(
#             text=request.POST['text'],
#             search=request.POST['search'],
#             email=request.POST['email'],
#             telephone=request.POST['telephone'],
#             created_at=datetime.datetime.now(),
#             updated_at=datetime.datetime.now(),
#             )
#             data.save()
#             astr = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
#             return JsonResponse({'data': 'success'})
#     else:
#         ajax_list = Ajax.objects.order_by('-created_at')
#         context = {'ajax_list': ajax_list}
#     return render(request, 'ajax.html',  {'ajax_list': ajax_list})
#
# @csrf_protect
# def getajax(request):
#     if request.method == 'GET':
#         if request.is_ajax():
#             data = Ajax.objects.order_by('-created_at').first()
#             created = data.created_at.strftime('%m-%d-%Y %H:%M:%S')
#             datas = {"id": data.id, "text": data.text, "search": data.search, "email": data.email, "telephone": data.telephone, "created_at": created}
#             return JsonResponse(datas)
#     else:
#         return JsonResponse({'data': 'failure'})
#
# @csrf_protect
# def ajax_delete(request):
#     if request.method == 'GET':
#         if request.is_ajax():
#             id=request.GET['id']
#             ajax = Ajax.objects.get(id=id)
#             ajax.delete()
#             return JsonResponse({'data': 'success'})
#     else:
#         return JsonResponse({'data': 'failure'})
#
#
# @csrf_protect
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#             username=form.cleaned_data['username'],
#             password=form.cleaned_data['password1'],
#             is_staff=True,
#             is_active=True,
#             is_superuser=True,
#             email=form.cleaned_data['email'],
#             first_name=form.cleaned_data['first_name'],
#             last_name=form.cleaned_data['last_name']
#             )
#             return HttpResponseRedirect('/register/success/')
#     else:
#         form = RegistrationForm()
#     return render(request, 'register.html', {'form': form})
#
# def register_success(request):
#     return render_to_response(
#     'success.html',
#     )
#
# @login_required
# def users(request):
#     users_list = User.objects.all()
#     paginator = Paginator(users_list, 5)
#     page = request.GET.get('page')
#     try:
#         users = paginator.page(page)
#     except PageNotAnInteger:
#         users = paginator.page(1)
#     except EmptyPage:
#         users = paginator.page(paginator.num_pages)
#     return render(request, 'users.html', {'users': users})
#
# @login_required
# def user_delete(request, id):
#     user = User.objects.get(id=id)
#     user.delete()
#     messages.error(request, 'User was deleted successfully!')
#     return redirect('/users')

@login_required
def upload_csv(request):
    if 'GET' == request.method:
        csv_list = CsvUpload.objects.all()
        paginator = Paginator(csv_list, 10)
        page = request.GET.get('page')
        try:
            csvdata = paginator.page(page)
        except PageNotAnInteger:
            csvdata = paginator.page(1)
        except EmptyPage:
            csvdata = paginator.page(paginator.num_pages)
        return render(request, 'crud/upload_csv.html', {'csvdata': csvdata})
    try:
        csv_file = request.FILES["csv_file"]

        if len(csv_file) == 0:
            messages.error(request, 'Empty File')
            return render(request, 'crud/upload_csv.html')

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return render(request, 'crud/upload_csv.html')

        if csv_file.multiple_chunks():
            messages.error(request, 'Uploaded file is too big (%.2f MB).' % (csv_file.size / (1000 * 1000),))
            return render(request, 'crud/upload_csv.html')

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        for index, line in enumerate(lines):
            fields = line.split(",")
            if index == 0:
                if (fields[0] == 'name') and (fields[1] == 'description') and (fields[2] == 'end_date') and (fields[3] == 'notes') and (fields[4] == 'images'):
                    pass
                else:
                    messages.error(request, 'File is not Correct Headers')
                    return render(request, 'crud/upload_csv.html')
                    break
            else:
                print(index)
                if (len(fields[0]) != 0) and (len(fields[1]) != 0) and (len(fields[2]) != 0) and (len(fields[3]) != 0) and (len(fields[4]) != 0):
                    data = CsvUpload(
                        name=fields[0],
                        description=fields[1],
                        end_date=datetime.datetime.now(),
                        notes=fields[3],
                        images=fields[4],
                    )
                    data.save()
        messages.success(request, "Successfully Uploaded CSV File")
        return redirect('/crudcsv/upload/csv/')

    except Exception as e:
        messages.error(request, "Unable to upload file")
        return redirect('/crudcsv/upload/csv/')

# @login_required
# def changePassword(request):
#     print('changepasword')
#     return render(request, 'change_password.html')



@login_required
def edit(request, id):
    members = CsvUpload.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

@login_required
def update(request, id):
    member = CsvUpload.objects.get(id=id)
    # member = CsvForm.objects.get(id=id)
    member.name = request.POST['name'],
    member.description = request.POST['description'],
    member.end_date = request.POST['end_date'],
    member.notes = request.POST['notes'],
    member.images = request.POST['images'],

    member.save()
    messages.success(request, 'Member was updated successfully!')

    return redirect('/crudcsv/upload/csv/')



@login_required
def delete(request, id):
    member = CsvUpload.objects.get(id=id)
    member.delete()
    messages.error(request, 'Member was deleted successfully!')
    return redirect('/crudcsv/upload/csv/')


# @login_required
# def create(request):
#     if request.method == 'POST':
#         # member = CsvUpload.objects.get(id=id)
#         member = CsvUpload(
#             name=request.POST['name'],
#             description=request.POST['description'],
#             end_date=request.POST['end_date'],
#             notes=request.POST['notes'],
#             images=request.POST['images'],)
#
#         try:
#             member.full_clean()
#         except ValidationError as e:
#             pass
#         member.save()
#         messages.success(request, 'Member was created successfully!')
#         return redirect('/crudcsv/upload/csv/')
#     else:
#         return render(request, 'crud/add.html')


# @login_required
# def create(request):
#     member = CsvForm(request.POST or None)
#
#
#     errors = None
#     if member.is_valid():
#         member.save()
#         return redirect("/crudcsv/upload/csv/")
#     if member.errors:
#         errors = member.errors
#     context = {
#         "member": member,
#     }
#
#     return render(request, 'crud/add.html', context)

class CreateCsv(CreateView):
    model = CsvUpload
    form_class = CsvForm
    success_url = reverse_lazy('upload_csv')

    template_name = 'crud/add.html'

 

