​    

[codewithstein.com](https://codewithstein.com/django-chat-using-channels-real-time-chat-tutorial-with-authentication/)

# Django Chat Using Channels - Real Time Chat Tutorial With Authentication | Code With Stein

------

## Setting up the environment

In this tutorial, I'm going to use a virtual environment for the project we're building. So the first thing we need to do is to instal  virtualenv. You can just run this command:

```
$ pip install virtualenv
```

Great, the next step now is to create a new environment and activate it.

```
$ virtualenv djangochat_env
$ source djangochat_env/bin/activate
```

So the first list here creates a new environment, and the second line activates it. When the environment is activated, we can start  installing packages for it.

We can install Django and Channels by running this command:

```
$ pip install django channels
```

First, this will install the latest version of Django and a few dependencies Django has. Next, it will install Channels.

**What is Channels?**
 I can quote the creators so it's easy to understand:
 "Channels wraps Django’s native asynchronous view support, allowing  Django projects to handle not only HTTP, but protocols that require  long-running connections too."

Perfect! All of the software we need is installed, so we can continue by creating a Django project and configuring it.

Creating a new Django project is really easy. We just run this command:

```
$ django-admin startproject djangochat
$ cd djangochat
```

I want to create a Django app for the core views like the front page, the sign up page and similar.

```
$ python manage.py startapp core
```

Even though we have created the app, Django doesn't know that it  doesn't exist. So we need to register it in a list of apps. So let's  open up the settings.py file.

Here, we can find a list called INSTALLED_APPS. There are a few built in apps from Django already, but we can just append 'core' at the  bottom.

```
'core',
```

We also need to tell Django about the channels package we installed. Let's add it below the 'core' app.

```
'channels'
```

There are two more configurations we need to do before we can start working on the front page.

First, we can tell Django where to look for the ASGI APPLICATION.  This can be added where ever you want, but let's put it together with  the WSGI APPLICATION.

```
ASGI_APPLICATION = "djangochat.asgi.application"
```

Then the last thing we need to do here is to set up the LAYERS configuration for Channels.

```
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
```

Instead of using something like Redis or similar, we're just going to use the servers memory for the messages. So before the messages are  stored in the database, they will live in the memory.

Great, the installation and configuration is now finished and we can start building the chat application.

## Creating the base and front page

​    Now that we have a project and an app for the core views, we can  continue to the next step which is to create a base template for the  project and a simple front page.

​    Let's begin by creating a new folder called "templates" in the core  app folder, and a folder called "core" inside the templates folder.    Django will automatically look for a folder called "templates"  inside each of the INSTALLED_APPS. The reason I have a folder called  "core" inside the templates folder is to make it easier to separate the  apps from each other.

​    Then we can create a new file called "base.html" inside the "core" folder. It should look like this:

```
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Djangochat</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css">
    </head>

    <body>
        <nav class="navbar is-dark is-purple pt-4 pb-4">
            <div class="navbar-brand">
                <a href="/" class="navbar-item is-size-4">Djangochat</a>
            </div>

            <div class="navbar-menu">
                <div class="navbar-end">
                    <a href="/login/" class="navbar-item">Log in</a>

                    <div class="navbar-item">
                        <a href="/signup/" class="button"><strong>Sign up</strong></a>
                    </div>
                </div>
            </div>
        </nav>
    </body>
</html>
```

This is a simple HTML file where we include [Bulma](https://bulma.io/) (A CSS framework) and a simple menu with the title and two buttons.

Great, let's create one more file called "frontpage.html" inside the  same folder. This file should extend and use the base.html file.

```
{% extends 'core/base.html' %}
```

Nice, we now have the two templates. But to render these and show  them in the browser, we need a view. So inside the core/views.py file,  create a new view for the frontpage.

```
def frontpage(request):
    return render(request, 'core/frontpage.html')
```

​    Then, the last step we need to do before we can test this is to  import the view into the urls.py file which is located in the  "djangochat" folder.    Modify it to look like this:

```
from django.contrib import admin
from django.urls import path

from core.views import frontpage

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('admin/', admin.site.urls),
]
```

​    What we have done here now is that we have imported the "frontpage" view we just created.     Then, we appended the path to this view into the list of urlpatterns.

​    The first argument is '', this means that when we go to the url for the page, we want it to use this view.     Next, we specify which view to use which is frontpage. Then the last argument name is the name of this view.     When we set this, we can refer to this page from other places in our project. I'll show you later in this project.

Great, now we can go to the command line and start the development server:

```
$ python manage.py runserver
```

Copy the address and open it in your browser. You should now see a simple page.

As you saw in the frontpage.html file, we extended the base.html file. But we didn't add any more data to it.

Do add data to it, we need to add some code blocks to the base.html file. Change the base.html like this:

```
# Change
<title>Djangochat</title>
# To
<title>{% block title %}{% endblock %}Djangochat</title>

# Below the nav bar, add this code block
{% block content %}
{% endblock %}
```

​    We now have the possibility to extend the template better.     Let's do some changes to the frontpage.html file as well.    Add this below the "{% extends 'core/base.html' %}" code.

```
{% block title %}Welcome | {% endblock %}

{% block content %}
    <div class="hero">
        <div class="hero-body">
            <h1 class="title has-text-centered has-text-white">Djangochat</h1>
        </div>
    </div>
{% endblock %}
```

​    I also want to add a little bit of styling to the page. This is just to make sure that the menu and background is purple.

```
<style>
    body {
        background: #9c88ff;
    }

    .navbar.is-purple {
        background: #8c7ae6;
    }

    .navbar .button {
        border-color: #9c88ff;
        background: #9c88ff;
        color: #fff;
    }
</style>
```

​    And that's it for the base.html file and the frontpage.     As you can see, information we write inside the code blocks in the templates that are extended,     will be rendered inside there in the other template.

## Sign up functionality

For the best security and simpleness, I want to use Django's built in UserCreationForm. Here, we will get a ready form we can use for signing up users and similar.

So the only thing we have to think about is telling Django which fields  to show and then create a template for rendering the form.

Inside the core app folder, create a new file called forms.py. It should look like this:

```
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
```

First we import a few things from Django. This is the UserCreationForm form class and the User database model.

Next we set up the SignUpForm where we use a meta class to configure  it. We need to specify which model to use (Which is User), and then  which fields we want the form to use.

We still have a few more steps we need to do. And the next step is to set up the view where we handle the post requests and similar.

So inside the views.py file in the core app folder, we first import  the SignUpForm we just created and then we create a new view for the  signup page.

```
from .forms import SignUpForm

def signup(request):
if request.method == 'POST':
    form = SignUpForm(request.POST)

    if form.is_valid():
        user = form.save()

        login(request, user)

        return redirect('frontpage')
else:
    form = SignUpForm()

return render(request, 'core/signup.html', {'form': form})
```

​    First we check if the request method is POST. That means that the form has been submitted.    And if it has, we can check if the form is valid and create/login the user.

​    If it's a normal request, we just create an empty instance of the form and render the template.

Next step now is the template. Create a new file called signup.html and add the following contents:

```
{% extends 'base.html' %}

{% block title %}Sign up | {% endblock %}

{% block content %}
<div class="hero">
    <div class="hero-body">
        <h1 class="title has-text-centered has-text-white">Sign up</h1>
    </div>
</div>

<section class="section has-text-white">
    <div class="columns">
        <div class="column is-4 is-offset-4">
            <form method="post" action=".">
                {% csrf_token %}

                {{ form.as_p }}

                <div class="field">
                    <div class="control">
                        <button class="button">Submit</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</section>
{% endblock %}
```

Most of this should look familiar. We add a csrf_token to the form to handle security. And then we just show/render the form easily as  paragraphs.

The last step before we can test this now is to add the view to the urls.py file.

```
# First, append the signup view here
from core.views import frontpage, signup

urlpatterns = [
    path('', frontpage, name='frontpage'),
    # Add this path
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),
]
```

Great. Now we can go to the browser and click the sign up button in the menu. Go ahead and create a new user.

## Log out functionality

When we sign up a new user, we are also automatically logged in. And  before we implement the log in functionality, I want to implement the  log out functionality.

Django has built in functionality for this, and I want to use it. So open up djangochat/urls.py and import this:

```
from django.contrib.auth import views as auth_views
```

We import this and rename it to auth_views. This makes it easier to separate from other views we import.

Next, we can append a new path to the urlpatterns:

```
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
```

Then the next step will be to show the log out button in the menu instead of log in/sign up when we are authenticated.

```
{% if request.user.is_authenticated %}
    <div class="navbar-item">
        <a href="/logout/" class="button">Log out</a>
    </div>
{% else %}
    <a href="/login/" class="navbar-item">Log in</a>

    <div class="navbar-item">
        <a href="/signup/" class="button"><strong>Sign up</strong></a>
    </div>
{% endif %}
```

Before you try this button, I just want to make sure that we are  redirected to the correct pages when we log out. Add these three lines  to the settings.py file:

```
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
```

LOGOUT_REDIRECT_URL = The page we are redicted to when we log out.
 LOGIN_REDIRECT_URL = The page we are redirected to after login.
 LOGIN_URL = The page for the login form.

Nice, now we can test the log out functionality before we start implementing the login functionality.

## Log in functionality

Just like we just Django's built in functionality for logging out, we are going to use it for logging in.

It's little bit more complicated now, since loggin in means that we need a login template.

Let's just begin with adding the path to the urlpatterns in the djangochat/urls.py file:

```
path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
```

As you can see where, we specify the things we need including the template we are going to create now.

Create a new file called login.html in the core template folder. It should look like this:

```
{% extends 'base.html' %}

{% block title %}Log in | {% endif %}

{% block content %}
<div class="hero">
    <div class="hero-body">
        <h1 class="title has-text-centered has-text-white">Log in</h1>
    </div>
</div>

<section class="section has-text-white">
    <div class="columns">
        <div class="column is-4 is-offset-4">
            <form method="post" action=".">
                {% csrf_token %}

                <input type="hidden" name="next" value="{{ next }}">

                <div class="field">
                    <label>Username</label>

                    <div class="control">
                        <input type="text" name="username" class="input">
                    </div>
                </div>

                <div class="field">
                    <label>Password</label>

                    <div class="control">
                        <input type="password" name="password" class="input">
                    </div>
                </div>

                {% if form.errors %}
                    <div class="notification is-danger">
                        Your username and password didn't match! Please try again!
                    </div>
                {% endif %}

                <div class="field">
                    <div class="control">
                        <button class="button">Submit</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</section>
{% endblock %}
```

The template is very easy and most of this should look familiar.

If there are any errors, we just show them using a Bulma  notification. There is also a hidden field called "next". This is the  URL you will be redirected to after you log in (If you come from a page  you didn't have access to).

## Create app for rooms

We need to create a new Django app for the rooms. Here we want  database models, consumers, views, templates and similar things that  will be connected to the rooms.

It's smart to split a Django project into many smaller Django apps because it makes everything more readable and maintainable.

So let's create a new app called "room":

```
$ python manage.py startapp room
```

​    And just like we added 'core' to the list of installed apps, we now need to append 'room' to the list as well.    So open up settings.py and add 'room', at the bottom of the list.

```
'room',
```

Next step then is to create the database model. A database model is  where we describe to Django what information we want to store in the  database.

Open up models.py and modify it to look like this:

```
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
```

We only want two fields for the Room model. This is a char field  which will be used to store the name of the room and a better name for  use in the URL.

Now that we have a database model for the rooms, we need to update  the database. So go to the command line and run the following command:

```
$ python manage.py makemigrations
```

This will create a few Python files with information about the  changes we are doing to the database. The database still hasn't been  updated, so we need to run one more command:

```
$ python manage.py migrate
```

​    What this command does is that it runs the Python files that was created when we executed the makemigrations command.    So now the database should be updated and we should have a table for our rooms.

## Create superuser

Django comes with an admin interface where we easily can add  information to the database. But in order to access this admin  interface, we need a super user.

To create this superuser, we need to run this command and follow the wizard:

```
$ python manage.py createsuperuser
```

If we now start the web server again, and go to http://127.0.0.1:8000/admin/, we can log in with the user we just created.

As you can see, you will now get the possibility to add users. But where is the Rooms model we just created?

Per default, models aren't automatically added to the list here. So we need to open up rooms/admin.py to add it.

```
from django.contrib import admin

from .models import Room

admin.site.register(Room)
```

Great, if we go back now and refersh. There will be a new option. Let's go ahead and add a few chat rooms to our application.

## Show list of rooms

To show the different chat rooms, I first want to create a new view for this. Open up room/views.py and add the following:

```
 # Import the Room database model
from .models import Room

# View for the rooms
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})
```

Here we just get all of the rooms from the database and add them to the context which will be available in the template.

Then, we can create the template which will list the rooms for us:

```
{% extends 'core/base.html' %}

{% block title %}Rooms | {% endblock %}

{% block content %}
<div class="hero">
    <div class="hero-body">
        <h1 class="title has-text-centered has-text-white">Rooms</h1>
    </div>
</div>

<section class="section has-text-white">
    <div class="columns is-multiline">
        {% for room in rooms %}
        <div class="column is-4 has-text-centered">
            <div class="box">
                <h2 class="subtitle">{{ room.name }}</h2>

                <a href="#" class="button">Join</a>
            </div>
        </div>
        {% endfor %}
    </div>
</section>
{% endblock %}
```

Here we're still extending the base.html template. In the columns, we use a for loop to loop through all of the rooms. We still cannot click  the Join button, but at least all of the rooms will be listed here.

To keep the main urls.py file as clean as possible, I want to create a separate urls.py file for the room app.

```
# room/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
]
```

You might notice that the path is empty here (just like the  frontpage). This is because in the main urls.py file, I want to pass  through all urls starting with "rooms" to this urls.py file.

Open up djangochat/urls.py. On the same line as we import path, append ", include" at the end like this:

```
from django.urls import path, include
```

And then inside the urlpatterns, append this path:

```
path('rooms/', include('room.urls'))
```

So if you go to "http://127.0.0.1:8000/rooms/" now, you will match  this path and sent to the room/urls.py file where you will match the  "empty" path.

Go ahead and visit that url now, and the rooms you created in the previous part should be listed out.

## Room detail view

Now it's time to make it possible to click a room. For this, we need a new view and template.

Let's open up room/views.py and add this view at the bottom:

```
def room(request, pk):
    room = Room.objects.get(pk=pk)

    return render(request, 'room/room.html', {'room': room})
```

As you can see, this is very similar to the rooms list view. The main difference is that we get an extra parameter in the view.

The extra paramater "pk" stands for primary key and will be an integer which will represent the ID for the room we want to join.

Next, we get the room from the database based on the primary key (pk).

Then, we just need to create a new template where we show the name of the room and a simple form.

```
{% extends 'core/base.html' %}

{% block title %}{{ room.name }} | {% endblock %}

{% block content %}
<div class="hero">
    <div class="hero-body">
        <h1 class="title has-text-centered has-text-white">{{ room.title }}</h1>
    </div>
</div>

<section class="section has-text-white">
    <div class="columns is-multiline">
        <div class="column is-8 is-offset-2">
            <div class="box messages" id="chat-messages">
                Messages will be displayed here...
            </div>
        </div>

        <div class="column is-8 is-offset-2">
            <div class="box">
                <div class="media">
                    <div class="media-content">
                        <form method="post" action=".">
                            <div class="field">
                                <div class="control">
                                    <input type="text" name="content" id="chat-message-input" class="input" placeholder="Your message...">
                                </div>
                            </div>

                            <div class="field">
                                <div class="control">
                                    <button class="button" id="chat-message-submit">Submit</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
{% endblock %}
```

Next step is to add this view to the list of urls in the room/urls.py file. Add this below the "rooms" path.

```
path('<int:pk>/', views.room, name='room'),
```

Here we say that we expect the url to contain an integer (the ID) and give it the name "pk" as you saw in the view.

Last step before we can test this now is to change the rooms.html a little bit. Replace the anchor tag with this:

```
<a href="{% url 'room' room.id %}">Join</a>
```

Here we use a built in template function from Django called 'url'.  This takes the name of a path (room) and a list of parameters.

So now this will automatically generate links looking like this: "/rooms/1/" and similar.

## Creating a consumer

Finally it's time to start implementing channels and making it possible to join a live chat.

The first step we need to do is to create something called a "consumer". The consumer will handle web socket traffic for us.

Let's create a new file called "consumers.py" in the room app folder. It should look like this(I added comments in the code to make it easier to understand):

```
# First we import json 
import json

from channels.generic.websocket import AsyncWebsocketConsumer # The class we're using
from asgiref.sync import sync_to_async # Implement later

# Create a consumer class
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
    # Join room based on name in the URL
    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = 'chat_%s' % self.room_name

    # Join room group
    await self.channel_layer.group_add(
        self.room_group_name,
        self.channel_name
    )

    await self.accept()

    async def disconnect(self, close_code):
    # Leave room group
    await self.channel_layer.group_discard(
        self.room_group_name,
        self.channel_name
    )
```

Nice. Just like we have a file called urls.py for our pages, we want a similar file for the web sockets.

Create a new file called "routing.py

```
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()), # Using asgi
]
```

There should already be a file called asgi.py in the djangochat  folder. This is entry points for traffic just like this. Open up  "djangochat/asgi.py" and make it look like this:

```
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})
```

## Joining a chat

First, we need to add a new code block to the base.html file so we  can pass in javascript. Add this code block before we close the body  tag.

```
{% block scripts %}{% endblock %}
```

Next step now is to add more functionality to the script inside  room.html to connect to the server. This should be added below the code  block for the content.

```
{% block scripts %}
{{ room.slug|json_script:"json-roomname" }}
{{ request.user.username|json_script:"json-username" }}

<script>
    const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
    const userName = JSON.parse(document.getElementById('json-username').textContent);

    const chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/'
        + roomName
        + '/'
    );

    chatSocket.onmessage = function(e) {
        console.log('onMessage');
    };

    chatSocket.onclose = function(e) {
        console.error('The socket closed unexpectedly');
    };
</script>
{% endblock %}
```

## Sending messages

We can also add the javascript for sending and receiving messages.

```
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    if (data.message) {
        document.querySelector('#chat-messages').innerHTML += ('<b>' + data.username + '</b>: ' + data.message + '<br>');
    } else {
        alert('The message was empty!')
    }
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': userName,
        'room': roomName
    }));

    messageInputDom.value = '';
};
```

Now everything in the frontend should be ready.

But there's still some thing that needs to be done in the backend.

```
# Receive message from WebSocket
async def receive(self, text_data):
    data = json.loads(text_data)
    message = data['message']
    username = data['username']
    room = data['room']

    # Send message to room group
    await self.channel_layer.group_send(
        self.room_group_name,
        {
            'type': 'chat_message',
            'message': message,
            'username': username
        }
    )

# Receive message from room group
async def chat_message(self, event):
    message = event['message']
    username = event['username']

    # Send message to WebSocket
    await self.send(text_data=json.dumps({
        'message': message,
        'username': username
    }))
```

So if we test now in two windows, we should be able to talk to eachother.

The problem now is that if we refresh, the messages are gone.

Or if you open one more window, the messages is also gone.

To fix this, we need to store the messages in a database.

## Storing messages

Open up "room/models.py" and add this new model.

```
class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
```

We also need to get the messages in the view.

```
# Import the messages model
from .models import Message

# Get the messages from the database
messages = Message.objects.filter(room=room)[0:25]

# Add the messages to the context
'messages': messages
```

So the whole "room" view should look like this now:

```
def room(request, pk):
    room = Room.objects.get(pk=pk)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})
```

And we need to add them to the template:

```
{% for m in messages %}<b>{{ m.user.username }}</b>: {{ m.content }}<br>{% endfor %}
```

So now we get the messages there, but we also need to store them when their sent. Open up the consumers.py file and make the following  changes:

```
# Import the user model
from django.contrib.auth.models import User

# Import the Message model
from .models import Room, Message

# Add a new method to the class
@sync_to_async
def save_message(self, username, room, message):
    user = User.objects.get(username=username)
    room = Room.objects.get(room=room)

    Message.objects.create(username=user, room=room, content=message)
# Place this line:
await self.save_message(username, room, message)

# Above this line
await self.channel_layer.group_send(
```

​    A little issue we have now is that when there are more than a few  messages, we will only see the messages at the top of the list.    So we want to set a maximum height, make the box scrollable and also send us automatically to the last message.

First, we can add a few lines of CSS to the base.html file:

```
.messages {
    height: 400px;
    overflow-y: auto;
}
```

Next, we are going to add JavaScript for the automatic scrolling. This can be done in the rooms.html file.

```
/**
* A function for finding the messages element, and scroll to the bottom of it.
*/
function scrollToBottom() {
    let objDiv = document.getElementById("chat-messages");
    objDiv.scrollTop = objDiv.scrollHeight;
}

// Add this below the function to trigger the scroll on load.
scrollToBottom();
```

And then add this line at the bottom of this function  (chatSocket.onmessage = function(e)) to trigger the scroll after a  message is sent:

```
scrollToBottom();
```

Great. So whenever we refresh the window or when there is a new message appearing, we will be sent to the bottom.

## Summary

​    That was it for this tutorial. You should now have a working chat application you can use.    It might not be ready for production, but with a few tweaks here and there, it most certainly can be used to anything.    The most obvious thing to change is to implement PostgreSQL instead of Sqlite.

​    If you want to learn even more about this subject, please check out my website [premium courses](https://codewithstein.com/courses/) where you can learn to build a Slack clone using the same technology.

## video :

https://www.youtube.com/watch?v=wLwu1NqU1rE&t=317s