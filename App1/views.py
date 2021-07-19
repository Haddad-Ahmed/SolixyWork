import collection as collection
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from App1.forms import ADDCollectionForm, CollectionModelForm, CollectionFilter
from App1.models import Collection
# Create your views here.

def index ( request) :
    return HttpResponse('SOLIXY')
def liste(request):
    return render(request, 'App1/Liste_Collection.html')
def add(request):
    return render(request, 'App1/Add_Collection.html')
def accueil(request):
    return render(request, 'Accueil.html')

def Collection_id(request, id ) :
    response ="identifiant du collection %s"
    return HttpResponse(response %id)

def Liste_Collection (request):
    Collections = Collection.objects.all()
    context = {'c' : Collections}
    return render(request, 'Accueil.html' , context)

class CreateCollection(CreateView):
    model = Collection
    fields = ['type', 'nom']
    success_url = reverse_lazy('List')
    
class DeleteCollection(DeleteView):
    model = Collection
    success_url = reverse_lazy('List')
    
class UpdateCollection(UpdateView):
    model = Collection
    fields = ['nom']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('List')
    
class DetailCollection(DetailView):
    model = Collection
    context_object_name='c'

class CollectionCreateView(BSModalCreateView):
    template_name = 'App1/collection/create_collection.html'
    form_class = CollectionModelForm
    success_message = 'Success: Collection was created.'
    success_url = reverse_lazy('List')

class CollectionUpdateView(BSModalUpdateView):
    model = Collection
    template_name = 'App1/collection/update_collection.html'
    form_class = CollectionModelForm
    success_message = 'Success: Collection was updated.'
    success_url = reverse_lazy('List')

# Read
class CollectionReadView(BSModalReadView):
    model = Collection
    template_name = 'App1/collection/read_collection.html'

# Delete
class CollectionDeleteView(BSModalDeleteView):
    model = Collection
    template_name = 'App1/collection/delete_collection.html'
    success_message = 'Success: Collection was deleted.'
    success_url = reverse_lazy('List')

def collection_list(request):
    f = CollectionFilter(request.GET, queryset=Collection.objects.all())
    return render(request, 'App1/collection/filtre_collection.html', {'filter': f})

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('LV')
        else:
            messages.info(request,'Username or Password is incorrect')
            return redirect('login')
    else:
        return render(request, 'App1/user/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.info(request,'Erreur')
            return redirect('signup')
    else:
        form=UserCreationForm()
        return render(request, 'App1/user/signup.html',{'f':form})