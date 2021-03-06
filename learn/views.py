from django.forms.forms import Form
from django.core.paginator import *
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from learn.models import *
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm
from learn.forms import CreateUserForm, CreateBioPage,ProfileImageUpdate,UpdateUserDetails
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from hitcount.views import HitCountDetailView
from django.db.models import Q
import redis
from django.conf import settings
from django.contrib.postgres.search import SearchQuery, SearchVector
# connect to redis
r = redis.Redis(host=settings.REDIS_HOST,
 port=settings.REDIS_PORT,
 db=settings.REDIS_DB)

# Create your views here.
def home(request):
    return render (request, 'home.html')
def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # user = authenticate(request, username=form.cleaned_data['username'],
            #                         password=form.cleaned_data['password1'],)
            # auth_login(request, user)
            user = form.cleaned_data.get('first_name')
            # get_username = form.cleaned_data.get('username')
            # x = User.objects.values('id').filter(username=get_username).first()
            # p=Profile(user_id=x['id'])
            # p.save()
            # bio_data = CreateUserBio.objects.filter(user=x['id'])
            messages.success(request,'congratulations ' + user + ' Your account is created you can login now!')
            return redirect('login')
    context = {'form': form, 'signupsucess': 'Congratulation you are logged in with successful signup process'}
    return render (request, 'signup.html', context ) 
    # else:
    #     if request.POST['password1'] == request.POST['password2']:
    #         try:
    #             user = User.objects.create_user(request.POST['username'], password =request.POST['password1'])
    #             user.save()
    #             auth_login(request, user)
    #             context = {'form': form, 'signupsucess': 'Congratulation you are logged in with successful signup process'}
    #             return render (request, 'signup.html',context )
            

    #         except IntegrityError:
    #             context = {'form': form, 'error': 'The username is already taken please use any other username'}
    #             return render (request, 'signup.html',context)
    #     else:
    #         context = {'form': form, 'error': 'Both Password did not match please type same password on both fields.'}
    #         return render (request, 'signup.html', context)
# def editProfile(request,id):
#     object = user.objects.get(id=id)
#     form = UserChangeForm(instance=object)
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('first_name')
#             messages.success(request,'congratulations ' + user + ' Your account is created you can login now!')
#             return redirect('profile')
    
#     context = {'form': form, 'signupsucess': 'Congratulation you are logged in with successful signup process'}
#     return render (request, 'editProfile.html', context )
       
    
def login(request):
    
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, username=username, password=password)
       
       if user is not None:
           auth_login(request, user)
           return redirect('home')
       else:
           messages.info(request, 'Username or password are not correct')
    
    context = {}
    return render (request, 'login.html', context)
def contact(request):
    context = {'success': False}
    if request.method=="POST":
        name    = request.POST['name']
        email   = request.POST['email']
        phone   = request.POST['phone']
        desc    = request.POST['desc']
        # print(name, email, phone, desc)
        ins     = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'contact.html', context)
    
@login_required(login_url='login')
def CreateBio(request):
    bio_data = CreateUserBio.objects.filter(user=request.user)
    if request.method == 'GET':
        return render (request, 'preview.html',{'bio_data': bio_data , 'form':CreateBioPage()} )  

    else:
        try:
            form         = CreateBioPage(request.POST)
            newlink      = form.save(commit=False)
            newlink.user = request.user
            newlink.save()
            return redirect('CreateBio')

        except ValueError:
            return render(request, 'preview.html',{'form':CreateBioPage(), 'error':'Bad data request'} )





def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    return redirect('home')

def loginuser(request):
    return render(request, 'login.html')


def profile(request):
    x      = Images.objects.filter(user=request.user)
    person = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'person':person})
# This view function helps to share the user data with unique url
def share(request, username, *args, **kwargs):
    try:
        u           = User.objects.get(username=username)
        x           = User.objects.values('id').filter(username=username).first()
        p           = CreateUserBio.objects.filter(user=x['id'])
        bio_data    = CreateUserBio.objects.filter(user=x['id'])
        person      = Profile.objects.get(user=x['id'])
        return render(request, 'explore.html', {'bio_data': bio_data,'u': u,'person': person,'p': p,})
    except User.DoesNotExist:
        g = username
        return render(request, 'usernotexist.html',{'g':g,})
        



class PostDetailView(HitCountDetailView):
    model               = Profile
    template_name       = 'explore.html'
    context_object_name = 'post'
    slug_field          = 'username'
    count_hit           = True

    
#     def share(request, username, *args, **kwargs):
#         u        = User.objects.get(username=username)
#         # u = User.objects.filter(user=request.user)
#         x        = User.objects.values('id').filter(username=username).first()
#         p        = CreateUserBio.objects.filter(user=x['id'])
#         bio_data = CreateUserBio.objects.filter(user=x['id'])
#         # all = CreateUserBio.objects.get(id=3)
#         #image = Images.objects.filter(user=x['id'])
#         person   = Profile.objects.get(user=x['id'])
#         return render(request, 'explore.html', {'bio_data': bio_data,'u': u,'person': person,'p': p})





def updatebio(request,pk_id):
    customer = get_object_or_404(CreateUserBio, pk=pk_id)
    if request.method == "POST":
        if request.user.is_authenticated:
          customer.delete()
        return redirect('CreateBio')
    return render(request, 'delete.html', {'customer': customer} )

def editProfile(request):
    if request.method == "POST":
        u_form = UpdateUserDetails(request.POST, instance=request.user)
        p_form = ProfileImageUpdate(request.POST, request.FILES,instance=request.user.profile.image.instance)
        # o_form = UserDetails(request.POST,instance=request.user.otherUserDetails)
        if u_form.is_valid() and p_form.is_valid(): # o_form.is_valid()
            u_form.save()
            p_form.save()
            # o_form.save()
            messages.success(request, f'Your profile is updated successfully')
            return redirect('profile')
    else:
        u_form = UpdateUserDetails(instance=request.user)
        p_form = ProfileImageUpdate(instance=request.user.profile.image.instance)
        # o_form = UserDetails(instance=request.user.otherUserDetails)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        # 'o_form': o_form,
    }
    return render(request, 'editProfile.html', context )

def intro(request):
    return render(request, 'intro.html')

    #CreateUserBio.objects.filter(id=id).delete()
    # updateBioDetails = get_object_or_404(CreateUserBio, pk=id)
    # deleteBioItem = CreateUserBio.objects.filter(id=id).delete()
    # return render(request, 'delete.html', {'deleteBioItem': deleteBioItem} )
# def previewBioPage(request, username):
#     # u = User.objects.get(pk=id)
#     u = User.objects.get(username=username)
#     # u = request.user.username
#     print(request.user)
#     x = User.objects.values('id').filter(username=username).first()
#     bio_data = CreateUserBio.objects.filter(user=x['id'])
#     return render (request, 'previewBioPage.html', {'bio_data': bio_data})
# from learn.pagination import *
# @pagination_classes((SearchPagination,))
def search_users(request):
    z=User.objects.all()
    a = request.GET.get('search')
    page_q = request.GET.get('p',1)
    
        # z = User.objects.filter(
        #     Q(first_name__icontains=a) | Q(last_name__icontains=a) |
        #     Q(username__icontains=a)
        # ).distinct()
    vector = SearchVector('first_name','last_name',)
    query = SearchQuery(a)
    z = User.objects.annotate(search=vector).filter(search=query)
    p = Paginator(z,5)
    
    #q = CreateUserBio.objects.filter(title__search=a)
    
    try:
        page = p.page(page_q) # this will return data of that particular page
    except PageNotAnInteger:
        page = p.page(1) # if the passed page is not Integer then first page is returned, you can customize this
    except EmptyPage:
        page = p.page(p.num_pages)
    # page = p.page(page_q)
    # q = CreateUserBio.objects.filter(title__search=a)
    return render(request, 'searchResult.html', {'page': page,'p': p})
    # else:
    #     q = None

    # except TypeError:
    #     return render(request, 'searchResult.html', {'Not found': q}) 
