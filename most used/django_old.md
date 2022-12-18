## preparing django project:

1) to know python libraries you installed

pip list

2) installing virtualenv:

pip install virtualenv

3) creating virtualenv:

virtualenv -p python3.8 dj4

4) cd dj4/

5) activate the virtualenv:
 
source bin/activate

6) installing django:

pip install django

7) making the src folder in dj4 :

mkdir src

8) cd src

9) if you need to clone a repo here , do it

10) starting the project :

django-admin startproject blog .

11) runnig server :

python manage.py runserver

12) to fix migrate error :

python manage.py migrate

13) to run the page:

http://127.0.0.1:8000/

14) to get in admin page :

http://127.0.0.1:8000/admin

15) creating superuser with username & password:

python manage.py createsuperuser

16) to start new app :

django-admin startapp post ( post is the name of the app)

17) after making database for the app you need to migrate these updates :

python manage.py makemigrations

python manage.py migrate

------------------------------------

## first connections in project

1) add the app (post) to the project (blog):

go to settings.py in blog then look for installed apps and add the app post :

'post',

2) create the database (tables) for the app post in models.py in app post:

```python

class Post(models.Model):

title=models.CharField(max_length=50)

content=models.TextField(max_length=1000)

created_at=models.DateTimeField()

class Meta:

verbose_name_plural = 'MyPosts' # MyPosts is the name that will be appear in # the admin pannel(django by default takes the table name and add s to it )

def __str__(self):

return self.title

```

4) to make this table appear in the admin page , go to admin.py in app post :

```python

from .models import Post

admin.site.register(Post)

```

5) in app post create file with the name urls.py and write this on it:

```python

from django.urls import path

from . import views #(to connect urls of app post with views of app post)

urlpatterns = [

path('',views.post_list)===> (post_list is a function in views off app post)

]

```

6) now we need to connect urls of the app post with urls of the project blog:

then go to urls of the project blog and write:

```python

from django.urls import path , include #( بسinclude دى هتلاقيها موجودة هتزود عليها )

from django.contrib import admin #(دى هتلاقيها موجودة اصلا مش هتعملها)

urlpatterns=[

path('admin/',admin.site.urls), #(دى موجودة لوحدها)

path('blog/' , include('post.urls')) #(here we connect urls of post with urls of blog)

]

```

7) go to views.py of the app post and write functions or classes to do something :

```python

from .models import Post #(to connect view with model)

def post_list(request):

all_posts= Post.objects.all()

return render(request,'post/all_posts.html',{'all_posts':all_posts})

# where all_posts.html is the template for this function (all_posts) in the app post

```

7. so we need to go to app post and create folder templates and create folder post on it and create a file in folder post with the name of all_posts.html)

8. go to all_posts.html and write html code and django code like:

```python

{% for post in all_posts %} #(this is the variable comes from post_list function)

{{post}}

{% endfor %}

```

-----------

## static & media files:

go to settings.py of your project (main project) then in the final of this file you will find this line:

STATIC_URL = '/static/'

so add these lines after it:

```python

STATICFILES_DIRS = [

BASE_DIR / "static",

'/var/www/static/',

]

MEDIA_URL = '/media/'

MEDIA_ROOT=BASE_DIR / "media"

```

then go to urls.py of your project to serve static files by this importing:

```python

from django.conf import settings

from django.conf.urls.static import static

```

also in the urls.py file put these after the list urlpatterns

```python

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

***note*** in the final of settings file of the main project you will find this link:

https://docs.djangoproject.com/en/3.2/howto/static-files/

that guids you in details to these things from documentation

-----------

## slug :

```python

# ex :

from django.db import models

from django.utils.text import slugify

class Post(models.Model):

title = models.CharField(max_length=255)

slug = models.SlugField(max_length=255, unique=True)

def save(self, *args, **kwargs):

if not self.slug:

self.slug = slugify(self.title)

super(Post, self).save(*args, **kwargs)

```

then go to admin.py where you register oyur table and make it like this to make slug be done automatically in admin panel :

```python

from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):

list_display = ('title',) # put all columns you need to appear in the admin panel

prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

```

----

## extend html file :

1) make a folder with name templates (put it beside project not in it or in any app)

2) make file base.html in templates folder

3) take the common html code in all html files in your project and put them in the base file and remove them from other files

4) make blocks in base.html file that suits other files with different names like:

{% block body %}

{% endblock body %}

5)) go to other files like home.html then make it like this

{% extends 'base.html' %}

{% block body %}

put here the code you removed from home.html before

{% endblock body %}

------

## get_absolute_url :

انت شغال مثلا فى صفحة الهوم وبتستخدم كلاس معين بتاخد منه البيانات زى ده :

```python

class Property(models.Model):

name = models.CharField(max_length=100)

image =models.ImageField(upload_to='property/')

price = models.IntegerField(default=0)

description = models.TextField(max_length=2000)

place= models.ForeignKey('Place',related_name='property_place',on_delete=models.CASCADE)

category = models.ForeignKey('Category',related_name='property_category',

on_delete=models.CASCADE)

slug = models.SlugField(null=True , blank=True)

def save(self, *args, **kwargs):

if not self.slug:

self.slug = slugify(self.name)

super(Property, self).save(*args, **kwargs)

def __str__(self):

return self.name

```

: وكده ودلوقت فيه زرار فى صفحة الهوم عايز ادوس عليه يودينى صفحة تانية , فيه طريقتين

* الطريقة المباشرة العادية

* get_absolute_url :

1) from django.urls import reverse

2) put this function in the class Property:

def get_absolute_url(self):

return reverse('property:propert_detail', Kwargs={'slug':self.slug})

where:

property is the name of url of the first page (home)

property_detail is the name of url of the page we want to go to

slug is the variable used in url of the page we want to go to

------

## pagination :

we have the view that come with the list of items that we need to paginate them:

```python

class PropertyList(ListView) :

model = Property

```

and we have the html pagination:

```html

<div class="row mt-5">

<div class="col text-center">

<div class="block-27">

<ul>

<li><a href="#">&lt;</a></li>

<li class="active"><span>1</span></li>

<li><a href="#">2</a></li>

<li><a href="#">3</a></li>

<li><a href="#">4</a></li>

<li><a href="#">5</a></li>

<li><a href="#">&gt;</a></li>

</ul>

</div>

</div>

</div>

```

all what we do :

1) define numbers of items to appear in every page (by putting on line in the view):

```python

class PropertyList(ListView) :

model = Property

paginate_by=6

```

2) modify the html to be like this:
```html

<div class="row mt-5">

<div class="col text-center">

<div class="block-27">

<ul>



<div class="row mt-5">

<div class="col text-center">

<div class="block-27">

<ul>

{% if page_obj.has_previous %}

<li><a href="?page={{ page_obj.previous_page_number }}">&gt;</a></li> <!-- previous -->

{% else %}

<li class="disabled"><span>&gt;</span></li>

{% endif %}

{% for i in paginator.page_range %}

{% if page_obj.number == i%}

<li class="active"><span>{{i}}</span></li> <!-- activated -->

{% else %}

<li><a href="?page={{i}}">{{i}}</a></li> <!-- pages -->

{% endif %}

{% endfor %}

{% if page_obj.has_next %}

<li><a href="?page={{ page_obj.next_page_number }}">&gt;</a></li> <!-- next -->

{% else %}

<li class="disabled"><span>&gt;</span></li>

{% endif %}

</ul>

</div>

</div>

</div>

```

**note ** django gives us a pagination

1) do the wiew step

2) you don't need the html pagination in the html page but just put this instead:

```html

{% for contact in page_obj %}

{# Each "contact" is a Contact model object. #}

{{ contact.full_name|upper }}<br>

...

{% endfor %}

<div class="pagination">

<span class="step-links">

{% if page_obj.has_previous %}

<a href="?page=1">&laquo; first</a>

<a href="?page={{ page_obj.previous_page_number }}">previous</a>

{% endif %}

<span class="current">

Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.

</span>

{% if page_obj.has_next %}

<a href="?page={{ page_obj.next_page_number }}">next</a>

<a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>

{% endif %}

</span>

</div>

```

------

## slider :

**video 3 from 13 to 19**

1) in the model of property app there is a relation ship(foriegnkey) between Property and

PropertyImage . this relationship has a name ==> property_image and we need these images

to be used in the slider

2) we just need to use html slider like this:

```html

<div class="single-slider owl-carousel">

{% for img in object.property_image.all %}

<div class="item">

<div class="hotel-img" style="background-image:url({{img.image.url}});"></div>

</div>

{% endfor %}

</div>

```

---------

## summernote :

use this link (a good explanaition) :

https://djangocentral.com/integrating-summernote-in-django/

-------

## related cards :

suppose we need to show cards related to the current card (related by category for example)

1) we have the current item details view :

```python

class PropertyDetail (DetailView):

#getting details of properties

model= Property

```

2) we add the function that get the related cards to this class:

```python

class PropertyDetail(DetailView):

#getting details of properties

model= Property

#getting related by the same category

def get_context_data(self,**kwargs):

context= super().get_context_data(**kwargs)

context["related"] = Property.objects.filter(category=self.get_object().category)[:2] # result is a list you can loop on it

return context

```

3. go to html related cards and loop them .

{% for property in related %}

{% endfor %}

---

## forms :

there are two ways to mkae form :

*) html form and use django to access it

*) use the django ready form :

1) create a file (forms.py) in the app you want the form in it

and put this on it :

```python

from django import forms

from .models import PropertyBook ===>PropertyBook is the name of the table we need to push information on it

class PropertyBookForm(forms.ModelForm):

#next two lines are used to show a calendar to choose a date

date_from = forms.DateField(widget= forms.DateInput(attrs={'id':'checkin_date'}))

date_to = forms.DateField(widget= forms.DateInput(attrs={'id':'checkin_date'}))

class Meta:

model = PropertyBook

fields = ['date_from','date_to','guest','children']

```

2) in views.py import these:

from django .views.generic.edit import FormMixin

from .forms import PropertyBookForm

3) in views.py in the class that get details of a property (becaus the form will be in the html file that is called by this class)

make this class inherit from FormMixin and call the form class from forms.py to this class like this:

form_class=PropertyBookForm

then make a function on the class with any name (post for example) like this:

def post(self,request,*args,**kwargs):

form = self.get_form()

if form.is_valid():

myform = form.save(commit=False)

myform.property = self.get_object()

myform.user = request.user

myform.save()

4) go to html file and go to the place you want the form to appear and put this:

{{form}}

5) to make the form be beautiful use django bootstrap4 , follow this link

https://github.com/zostera/django-bootstrap4

so in this link it will give you a template example so copy it and

put it in the html file instead of {{form}} in number 4

this template is :

<form action="/url/to/submit/" method="post" class="form">

{% csrf_token %}

{% bootstrap_form form %}

{% buttons %}

<button type="submit" class="btn btn-primary">Submit</button>

{% endbuttons %}

</form>

####################django filter############33

we will use a ready library that called django_filter , follow this link:

https://github.com/carltongibson/django-filter

or these steps:

1) pip install django-filter

2) add it to installed apps:

INSTALLED_APPS = [

...

'django_filters',

]

3) create a file (filters.py) and put this on it:

import django_filters

from .models import Property ===> property is the model(table) i use to filter

class PropertyFilter(django_filters.FilterSet):

class Meta:

model = Property

fields = ['name', 'description', 'place','category']

4) go to views.py and import these :

from .filters import PropertyFilter

from django_filters.views import FilterView

5) in views.py in the class that get the item list that inherit

from ListView we just remove ListView and make it inherit

from FilterView instead (this won't affect items list becaus

FilterView actually inherits from ListView )

and add this in this class:

filterset_class = PropertyFilter ===> this is the class we made in the file filters.py to make this view use this class in filtering

template_name = "property/property_list.html" ===> we said that FilterView inherits from ListView but unfotunately it doesn't inherit the html rendered path so we added it here

6) now go to html file (property_list.html) to connect with filter form there:

1) remove the exist filter html part

2) {% load bootstrap4 %}

3)put this instead of filter html part you just removed:

<form class="form">

{% csrf_token %}

{% bootstrap_form filter.form %}

{% buttons %}

<button type="submit" class="btn btn-primary">Search</button>

{% endbuttons %}

</form>

############another way to search ######################

we have this class in views:

class PostList(ListView):

model = Post

and we have this form in the frontend:

<form action="#" class="search-form">

<div class="form-group">

<span class="icon fa fa-search"></span>

<input type="text" class="form-control" placeholder="Type a keyword and hit enter">

</div>

</form>

so:

1) we add method='GET' and add the url we need to go when we type the search button and give the button a name (for example name='q') so the form will be like this:

<form action="{% url 'blog:post_list' %}" method='GET' class="search-form">

<div class="form-group">

<span class="icon fa fa-search"></span>

<input type="text" name='q' class="form-control" placeholder="Type a keyword and hit enter">

</div>

</form>

2)go to views and put this function in the class PostList:

def get_queryset(self):

name = self.request.GET.get('q','')

object_list = Post.objects.filter(

Q(title__icontains=name) |

Q(description__icontains=name)

)

return object_list

###############filtering by what is comming from url########

(الجزء ده للفلتر اللى فى يمين صفحة الديتيلز هيطبق على التاجز وهتعمل واحد زيه للكاتيجوريز)

for example ==> searching by tags

1) make this class in views:

class PostsByTags(ListView):

model = Post

2) in urls.py put this in urlpatterns:

path('tags/<slug:slug>' ,views.PostsByTags.as_view(), name='post_by_tags'),

3) in views:

from django.db.models.query_utils import Q

4)put this function in the class you made in number 1 (PostsByTags):

def get_queryset(self):

slug = self.kwargs['slug']

object_list = Post.objects.filter(

Q(tags__name__icontains=slug)

)

return object_list

4) go to html:

href="{% url 'blog:post_by_tags' tag %}"

##########################date##########################

to customize date in django :

search django template filters and look for date on them

ex:

{{post.created_at|date:'F j Y'}}

##################tags##############################

search ==> djangopackages and find taggit then follow its github guid

install taggit :

pip install django-taggit

then add it to installed apps

1)import it in models.py:

from taggit.managers import TaggableManager

2) put it as a field in the model(table) you want:

tags = TaggableManager()

3)the tags part in html will be:

<div class="tag-widget post-tag-container mb-5 mt-5">

<div class="tagcloud">

{% for tag in post.tags.all %}

<a href="#" class="tag-cloud-link">{{tag}}</a>

{% endfor %}

</div>

</div>

###################################################

to count number of posts in every category :

1) from django.db.models import Count

2) in get_context_data function put this :

context["categories"] = Category.objects.all().annotate(post_count=Count('post_category'))

where post_category is the related name of the relatioinship between Post model and Category models

3) call it in the frontend using property_count

ex: {% for place in places %}

<H1>place.property_count</H2>

{% endfor %}

**note** مش لازم دالة كونتيكست لكن اى دالة عادى

ex:

def home(request):

places=Place.objects.all().annotate(property_count=Count('property_place'))

#####################report data as pdf for example ################

search for ==> django advanced reports or find it in djangopackages Website

##########################footer####################################

لو عندنا جزء ثابت فى كل اصفحات زى الفوتر فاخنا هنعمله مرة واحد ونستدعيه بعد كدة

1) create a new file in app settings with the name ==>footer_context_processor.py

2) write this function in this file: (هنرجع بيانات جدول السيتنجس اللى هنملأ بيها الفوتر)

from .models import Settings

def myfooter(request):

myfooter = Settings.objects.last()

return {'myfooter':myfooter} ==> هنا بنرجع البيانات دى ككونتكست بس يعنى معملنلهاش رندر فى اى صفحة ات تى ام ال

3) go to settings of the project and look for TEMPLATES and find 'context_processors' in it

then add this to them:

'settings.footer_context_processor.myfooter',

4) go to base.html (because all other files inherit from it) and call data on it

for example the name will be called like this ==> myfooter.site_name

where myfooter is the context data from the function and site_name is the name of the site from settings models

#########################search home #######################

search and give results in another page:

1) in views put this function:

def home_search(request):

pass

2) connect this function to a url :

put this in urlpatterns:

path('search', home_search , name='home_search')

3) go to search form in the html and make these in the form:

* method="get" ==> because we take data from username

* action="{% url 'home:home_search' %}" ==> it is the path that the form will go to it when the user click its submit button

(home is the url that go to home.html page that contains the search form)

(home_search is the url that go to the function home_search to execute)

4)weneed to receive data from the text input and select button from the form to use in the backend:

* go to the text input in the form (where we will write what we look for)

and give it a name ===> name='name'

* go to the select (menu that we select an option from it) in the form

and give it a name ===> name='place'

5) now you can recieve these data from the form in the backend by updating

the function in views to be like this:

def home_search(request):

name=request.Get.get('name')

place=request.GET.get('place')

print(name , place) ==>will print (in cmd) what user entered in the front

6) now we need to use Q to search:

from django.db.models.query_utils import Q

def home_search(request):

name=request.Get.get('name')

place=request.GET.get('place')

property_list = Property.objects.filter(

Q(name__icontains = name) &

Q(place__name__icontains = place)

)

return render(request,'settings/home_search.html',{'property_list':property_list})

where home_search.html is the page that we need the search result to appeare on it

and it is the same of property_list.html but with small backend modify

######################### empty #####################

to show sothing if there is no result :

{% for %}

html code

{% empty %}

html code ex==> <h5> no result </h5>

{% endfor %}

#####################first foorloop###################################

ex:

{% for faq in object_list %}

<div class="card">

<div class="card-header">

<a class="card-link" data-toggle="collapse" href="#menu{{faq.id}}" aria-expanded="true" aria-controls="menuone">{{faq}}<span class="collapsed"><i class="icon-plus-circle"></i></span><span class="expanded"><i

class="icon-minus-circle"></i></span></a>

</div>

<div id="menu{{faq.id}}" class="collapse {% if forloop.first %} show {% endif %}">

<div class="card-body">

<p>{{faq.description}}</p>

</div>

</div>

</div>

{% endfor %}

#############user accounts############################

1) create app with name accounts

2) add the app to installed_apps in project settings

and create file urls.py

3) we know that django has a table called User that contains:

first_name

last_name

user_name

email

password

so we need also to make user have nor information like :

phone_number

address

image

so go to models.py in this app and create a new table (class)

with name Profile and relate it to django User table :

from django.contrib.auth.models import User

class Profile(models.Model):

user = models.OneToOneField(User, on_delete=models.CASCADE)

phone_number = models.CharField(max_length=30)

address= models.CharField(max_length=150)

image=models.ImageField(upload_to='users/')

def __str__(self):

return self.user

4) add this table to admin.py :

from .models import Profile

admin.site.register(Profile)

5) we need to make signal that when a new user created

it will create a profile immediately to this user

so go to models.py and put this after our Profile class(after it not in it):

from django.db.models.signals import post_save

from django.dispatch import receiver

@receiver(post_save, sender=User)

def create_user_profile(sender, instance, created, **kwargs):

if created:

Profile.objects.create(user=instance)

**note** for more details visite this link:

https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html

6) now , django gives us an url to add in the main urls.py of project:

path('accounts/', include('django.contrib.auth.urls')),

this url will provide these automatically with no need to write them:

accounts/ login/ [name='login']

accounts/ logout/ [name='logout']

accounts/ password_change/ [name='password_change']

accounts/ password_change/done/ [name='password_change_done']

accounts/ password_reset/ [name='password_reset']

accounts/ password_reset/done/ [name='password_reset_done']

accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']

accounts/ reset/done/ [name='password_reset_complete']

7)repair authentication html files as following:

*go to accounts app

*create folder templates on it

*create folder registration on templates

*create these html files in registration folder:

logged_out.html

login.html

password_reset_complete.html

password_reset_confirm.html

password_reset_done.html

password_reset_email.html

password_reset_form.html

password_change_form.html

sign_up.html

profile.html

edit_profile.html

* to fill these html files with their html code go to this site :

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication

but you won't find the code of password_change_form.html so here it is:

<form action="" method="post">

{% csrf_token %}

{{form}}

<input type="submit" class="btn btn-default btn-lg" value="Change password">

</form>

or the code of sign_up.html so here it is:

<h2>Sign up</h2>

<form method="post">

{% csrf_token %}

{{ form.as_p }}

<button type="submit">Sign up</button>

</form>

or the code of profile.html so here it is:

<h1>my profile</h1>

{{profile}}

{{profile.user.username}}

{{profile.user.first_name}}

{{profile.user.last_name}}

{{profile.phone}}

{{profile.email}}

or the code of edit_profile.html so here it is:

<h2>Profile Edit</h2>

<form method="post">

{% csrf_token %}

{{user_form}}

{{profile_form}}

<input type="submit" value="Edit Profile">

</form>

8) here will be some problems like when you go to password_reset url for example it will

take you to this part in the admin page not to the html form you made

sp the solution is :

check that app accounts is befor admin in installed_apps in settings

check that url accounts is befor admin in the main urls.py in project

9) now these all pages are ready by django and their views also ready by django axcept three parts:

Profile

edit Profile

sign up

so we will make three functions in views to handle them:

from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate

from .forms import SignUpForm

def profile(request):

profile = Profile.objects.get(user=request.user)

return render(request ,'registration/profile.html', {'profile':profile})

def edit_profile(request):

profile = Profile.objects.get(user=request.user)

if request.method == 'POST':

user_form=UserForm(request.POST , instance=request.user)

profile_form= ProfileForm(request.POST , instance=profile)

if user_form.is_valid() and profile_form.is_valid():

user_form.save()

myprofile=profile_form.save(commit=False)

myprofile.user=request.user

myprofile.save()

return redirect('/accounts/profile')

else:

user_form=UserForm(instance=request.user)

profile_form= ProfileForm(instance=profile)

return render(request, 'registration/edit_profile.html', {

'user_form': user_form ,

'profile_form':profile_form

})

def sign_up(request):

if request.method == 'POST':

form = SignUpForm(request.POST)

if form.is_valid():

form.save() # if form is valid it will sucsess it and store data in data base

#next part is for logging in directly after signing up

# we do this part if we need that user can sign up and login in directly without going to login page

#but if we need user to login again after signing up we remove the next part and make

#this function redirect to login page instead of home page

username = form.cleaned_data.get('username')

raw_password = form.cleaned_data.get('password1')

user = authenticate(username=username, password=raw_password)

login(request, user)

#end logging in part

return redirect('/') # go to home after sign up and login in success

else:

form = SignUpForm()

return render(request, 'registration/sign_up.html', {'form': form})

then create urls to them in urls.py in the accounts app:

from django.urls import path

from .views import profile , edit_profile , sign_up

urlpatterns=[

path('profile',profile , name = 'profile'),

path('edit_profile', edit_profile , name='edit_profile'),

path('sign_up', sign_up, name='sign_up'),

]

then connect them all to the main urls.py of the project:

path('accounts/', include('accounts.urls',namespace='accounts')),

10) create a new file forms.py in accounts app

and put this on it:

from django import forms

from accounts.models import Profile

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

# for sign up part

class SignUpForm(UserCreationForm):

class Meta:

model = User

fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

#end sign up part

# next two classes are for edit_profile part

#we need to collect these two tables in one table to be able to edit them in one time

class UserForm(forms.ModelForm):

class Meta:

model = User

fields = ['username','email','first_name','last_name']

class ProfileForm(forms.ModelForm):

class Meta:

model = Profile

fields = ['image','phone_number','address']

####################making login , signup , profile buttons in navbar###############

put these in navbar in ul :

{% if request.user.is_authenticated %}

<li class="nav-item cta"><a href="{% url 'accounts:profile' %}" class="nav-link"><span>Profile</span></a></li>

{% else %}

<li class="nav-item cta"><a href="{% url 'login' %}" class="nav-link"><span>Login</span></a></li>

<li class="nav-item cta"><a href="{% url 'accounts:sign_up' %}" class="nav-link"><span>Signup</span></a></li>

{% endif %}

############average rating calculation & check availability of a property##############3

go to model (table) of the thing you want to rate or check availability of it it (property)

and make a function (like get_absolute_url) inside this table class:

def get_average_rating(self):

ratings=self.reviw_property.all() # where reviw_property is the related name between the two tables

ratings_sum=0

if len(ratings) > 0 :

for rating in ratings:

ratings_sum += rating.rate

return round(ratings_sum/len(ratings),2)

else:

return 'no reviews'

def check_availability(self):

all_reservations = self.book_property.all() # where book_property is the related name between the two tables

now=timezone.now()

for reservation in all_reservations:

if now > reservation.date_to:

return 'available'

elif now > reservation.date_from and now < reservation.date_to:

reserved_to = reservation.date_to.date()

return f'not available until {reserved_to}'

else:

return 'available'

to make ratings and check_availability appear in admin as a table :

go to admin.py of this app and create class to do this:

class RatingAverageAndCheckAvailability(admin.ModelAdmin):

list_display = ['name','price','get_average_rating','check_availability']

and add this class name to be registered with the table on it:

admin.site.register(Property,RatingAverageAndCheckAvailability) ===> note that you can't add more than a class to be registered with a table

so if there is another class you want to add it to the same table you have to merge them like this:

class PropertyDescriptionAdmin(SummernoteModelAdmin):

summernote_fields = ('description',)

list_display = ['name','price','get_average_rating','check_availability']

admin.site.register(Property,PropertyDescriptionAdmin)

******************************

to make check_availability results appear in html :

go to the part of html code you want it to appear on it and put this:

{% if property.check_availability == 'available' %}

<h4>Available today</h4>

{% else %}

<h4>This Property is booked until {{property.check_availability}}</h4>

{% endif %}

**************************

another example: (check_reservation)

we need to make a function to show if the property is reserved or not (هيظهر قدام كل واحدة علامة صح او غلط على حسب هى محجوزة ولا لا)

go to model (table) of the thing you want to rate or check availability of it it (property)

and make a function (like get_absolute_url) inside this table class:

def check_reservation(self):

now = timezone.now()

return now > self.date_from and now < self.date_to

check_reservation.boolean = True # هنا بقوله يفعل البوليان للفانكشن دى , لو معملتش السطر ده هيطلعلى ترو وفولس بدل صح و غلط

go to admin.py of this app and create class to do this:

class ShowingReservation(admin.ModelAdmin):

list_display = ['property','check_reservation']

admin.site.register(PropertyBook,ShowingReservation)

######################## Api ######################

installing:

1)

pip install djangorestframework

pip install markdown # Markdown support for the browsable API.

pip install django-filter # Filtering support

2)

INSTALLED_APPS = [

...

'rest_framework',

]

3) add this to the mail url of the project :

urlpatterns = [

...

path('api-auth/', include('rest_framework.urls'))

]

***********************

using:

ex: getting the api for the post list of blog (the app name is blog & the table (model) name is Post )

1) create serializers.py (something like forms.py to define fields of the table needed to be serialized)file in the app blog then put this on it

from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):

class Meta:

model = Post

fields = '__all__'

2) create api_view.py file in the app blog then put this on it to get all posts and post details to be apis:

from .models import Post

from .serializers import PostSerializer

from rest_framework.response import Response

from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

@api_view(['GET'])

def post_list_api(request):

all_posts = Post.objects.all()

data = PostSerializer(all_posts , many=True).data

return Response({'data':data})

@api_view(['GET'])

def post_detail_api(request , id):

# i need to get the post where id of the table = id comming in the url

post= get_object_or_404(Post , id=id) # if it doesn't find the requested post it will give error 404 page

data = PostSerializer(post).data

return Response({'data':data})

3) create urls to these two functions in urls.py of the app blog:

path('api/list',post_list_api,name='post_list_api'),

path('api/list/<int:id>',post_detail_api,name='post_detail_api'),

**************************

we can use class based view instead function :

ex: to get post list :

from rest_framework.generics import ListAPIView

class PostListApi(ListAPIView):

queryset=Post.objects.all()

serializer_class= PostSerializer

****************** http methods ****************

GET =====> to get data from database

POST ====> to put new data in database

PUT =====> to modify data in database

DELETE ==> to delete data from database

############api search ###############

from django.db.models.query_utils import Q

@api_view(['GET'])

def post_search_api(request , query): # query is (الكلمة اللى هتبحث بيها)

posts = Post.objects.filter(

Q(title__icontains=query) |

Q(description__icontains=query)

)

data = PostSerializer(posts , many=True).data

return Response({'data':data})

************ api user authentications *************

1) pip install dj-rest-auth

2)INSTALLED_APPS = (

...,

'rest_framework',

'rest_framework.authtoken',

...,

'dj_rest_auth'

)

3)

urlpatterns = [

...,

path('rest-auth/', include('dj_rest_auth.urls'))

]

4)python manage.py migrate

5)

INSTALLED_APPS = (

...,

'django.contrib.sites',

'allauth',

'allauth.account',

'allauth.socialaccount', # this is to register using socialmedia apps like facebook,google

'dj_rest_auth.registration',

)

SITE_ID = 1

6)

urlpatterns = [

...,

path('dj-rest-auth/', include('dj_rest_auth.urls')),

path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))

]

**note** this alla explained in details here :

https://dj-rest-auth.readthedocs.io/en/latest/installation.html

*********************tokens*********************************

1) go to api_view.py:

from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view, permission_classes

2) if you use function based view:

add this to the function after @api_view(['GET']) and befor the function:

@permission_classes([IsAuthenticated]) # يعنى متقدرش توصل للدالة دى الا اذا كان ليك سماحية الوصول ليها

if you use class based view:

put this inside the class (the first thing inside the class):

permission_classes = [IsAuthenticated]

3) go to settings and add this under INSTALLED_APPS

REST_FRAMEWORK = {

'DEFAULT_AUTHENTICATION_CLASSES': [

'rest_framework.authentication.TokenAuthentication',

]

}

4) now if you run the url that shows this function api result you will get this message:

"Authentication credentials were not provided." ===>يعنى ملكش صلاحية الوصول

(لانك محتاج تديله التوكين بتاعك علشان تقدر تأكسس على الجزء ده)

5) testing token in postman:

Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

*************** api documentation ***********************

two ways to make api documentation :

*way one:by using swagger library :

look for django rest swagger then you will find its github explanation :

you just install it , add it to installed apps , put its url

then go to this url in the browser , you will find the documentation is ready.

*way two: using postman:

mahmoud ahmed ==> api part 2 from minute 39 to 57

----

## general notes :

### importing User table

```python

from django.contrib.auth.models import User

#user = models.ForeignKey(User,related_name='user', on_delete=models.CASCADE)

```

### choices :

```python

user_types = [

('admin', 'Admin'),

('doctor', 'Doctor'),

('student', 'Student'),

]

# user_type = models.CharField( max_length=50, choices=user_types ,default='student')

```

### upload to :

```python

image = models.ImageField(upload_to='media/' , null = True , blank = True)

```