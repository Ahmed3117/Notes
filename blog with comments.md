## Build a simple blog using Django 3 in under 20 minutes 

------

Learn how to quickly set up a simple blog using Django 3. The blog will have posts and comments.            

## Table of contents

- [Installation and setup](about:reader?url=https%3A%2F%2Fcodewithstein.com%2Fbuild-a-simple-blog-using-django-3-in-under-20-minutes%2F#installationandsetup)
- [The blog app](about:reader?url=https%3A%2F%2Fcodewithstein.com%2Fbuild-a-simple-blog-using-django-3-in-under-20-minutes%2F#theblogapp)
- [Post database model](about:reader?url=https%3A%2F%2Fcodewithstein.com%2Fbuild-a-simple-blog-using-django-3-in-under-20-minutes%2F#postdatabasemodel)
- [Django admin interface](about:reader?url=https%3A%2F%2Fcodewithstein.com%2Fbuild-a-simple-blog-using-django-3-in-under-20-minutes%2F#djangoadmininterface)
- [The front page](about:reader?url=https%3A%2F%2Fcodewithstein.com%2Fbuild-a-simple-blog-using-django-3-in-under-20-minutes%2F#thefrontpage)
- [List of blog posts](about:reader?url=https%3A%2F%2Fcodewithstein.com%2Fbuild-a-simple-blog-using-django-3-in-under-20-minutes%2F#listofblogposts)
- [Detail view of blog post](about:reader?url=https%3A%2F%2Fcodewithstein.com%2Fbuild-a-simple-blog-using-django-3-in-under-20-minutes%2F#detailviewofblogpost)
- [Adding comments](about:reader?url=https%3A%2F%2Fcodewithstein.com%2Fbuild-a-simple-blog-using-django-3-in-under-20-minutes%2F#addingcomments)
- [Displaying comments](about:reader?url=https%3A%2F%2Fcodewithstein.com%2Fbuild-a-simple-blog-using-django-3-in-under-20-minutes%2F#displayingcomments)
- [Video version of this post](about:reader?url=https%3A%2F%2Fcodewithstein.com%2Fbuild-a-simple-blog-using-django-3-in-under-20-minutes%2F#video)
- [Summary](about:reader?url=https%3A%2F%2Fcodewithstein.com%2Fbuild-a-simple-blog-using-django-3-in-under-20-minutes%2F#summary)

## Installation and set up

I always recommend using a virtual environment. This makes it easier to deploy and maintain.

So the first thing we are going to do is to create a new virtual environment.

```
$ virtualenv codewithstein_3_6_4
```

"codewithstein" is the name of our project and "3_6_4" is the version of Python I run on my Mac. Don't worry if this is a little bit  different than your version.

Next step is to go into the environment and activate it.

```
$ cd codewithstein_3_6_4
$ source bin/activate
```

Now that we have a virtual enviroment activated, we can install Django.

```
$ pip install django
```

This will install the newest stable version of Django into the  environment. So if you try to use Django outside of this environment, it will not work.

Last step of this section is to create a Django project. Just run this simple command:

```
$ django-admin startproject codewithstein
```

Now we have created a Django project and we're ready to start coding.

## The blog app

Usually, a Django project consist of many smaller apps. In our  project, we are going to have an app for the blog. This will cover the  posts and the comments. It isn't too complicated, to splitting this into more apps isn't necessary.

To create the app, we first need to go into the root of our Django project and then run a simple command.

```
$ cd codewithstein
$ python manage.py startapp blog
```

"manage.py" is a file we got when we created the Django project. This is a script for running administrative tasks like creating apps,  updating the database and similar.

Perfect! Let's continue by opening the project in an editor. I like to use [Visual Studio Code](https://code.visualstudio.com/).

When you have open the project in an editor, I want to begin by  creating a folder inside the blog app called "templates". Django will  automatically look for a folder called "templates" inside all of the  apps. Inside the templates folder, I want to create one more folder  called "blog". This will make it easier to separate the apps from each  other later.

The last step of this section is to register the blog app with  Django. Django doesn't know that it exists, so we need to add it to a  list.

Open up "settings.py" and append "blog" to the bottom of the list of  INSTALLED_APPS. The "settings.py" file is configuration for the project. Here you can find options for the templates, database, security and  similar.

## Post database model

First of all, what is a database model?
A database model is a  Python class we use to describe to Django what the content is. If we  take a blog post for example, we would need a title, slug, intro, body  and maybe a time stamp.

To create the database model for the post, open up "blog/models.py". We need to add some code here.

```
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
    	ordering = ['-date_added']
```

- "Post" is the name of the database model.
- "title" uses a field type called CharField. This is just a simple line of text. Here we need to set a max_length option.
- "slug" uses a field type called SlugField. This is the address to the blog post.
- "intro" and "body" uses a field type called TextField. These are fields for holding big chunks of text.
- "date_added" uses a field type called DateTimeField. This will  store information about when it was created. We add a  "auto_now_add=True" option to this field. This will tell Django to  automatically add "now" when we create a new blog post.
- We also add a sub class here called Meta. This is configuration for the model. We want to change the ordering so we can get the newest post on top.

Great, we now have a database model. But it still hasn't been added  to the database. To do this, we need to go to the command line and run  two commands.

```
$ python manage.py makemigrations
$ python manage.py migrate
```

The first command will generate files containing information about  the different models and changes we have done to them. The second  command will run a migrate script and update the database.

## Django admin interface

Django comes with a built in admin interface. This makes it really easy to add data to our project.

The first thing we need to do is to create a user who can access this area.

```
$ python manage.py createsuperuser
```

Just follow the wizard and type the required information.

Perfect, let's fire up Django's built in web server and log in to Django admin.

```
$ python manage.py runserver
```

Open up http://127.0.0.1:8000/admin/ in your browser and log in with the user you just created.

As you can see here, you will get access to the users and groups. But the Post model isn't there yet. We need to register the model with the  admin area first. Luckily for us, this is really simple.

Open up "blog/admin.py".

```
from .models import Post
admin.site.register(Post)
```

First we import the Post model, then we register it. Let's go back to the browser and refresh.

As you can see, we can now see a new row for the Post model.

Click add to create a new blog post.

## The front page

Since we have some data in our database now, we can start thinking about creating a front page to display a list of blog posts.

Create a new file called "base.html" inside the "templates/blog" folder.

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Code With Stein</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css">
  </head>

  <body>
    <nav class="navbar">
      <div class="navbar-brand">
        <a href="/" class="navbar-item"><strong>Code With Stein</strong></a>
      </div>
    </nav>
    
    <section class="section">
      <div class="container">
        {% block content %}
        {% endblock %}
      </div>
    </section>
  </body>
</html>
```

Most of the code here should look familiar if you know basic HTML. I  include a CSS framework called Bulma. I use this so I don't have to  think too much about the design for this tutorial.

Inside the body, I add a simple menu and a section to hold all of the content.

I added a simple template block. This makes it possible to re-use  this template and just extend it for all of the pages. You will probably understand more when I create the template for the front page.

Let's just continue and create a new file called "frontpage.html" in the same folder as "base.html".

The front page template will just extend the base template, so it will look much simpler.

```
{% extends 'blog/base.html' %}

{% block content %}
	<h1>This is the front page</h1>
{% endblock %}
```

What happens now is that all the HTML we put inside the block here,  will be rendered inside the block in the base.html file. You can have as many blocks as you want.

To show this template to the visitors, we need a view. These are located in the "views.py" file inside the app.

```
def frontpage(request):
    return render(request, 'blog/frontpage.html')
```

This wasn't complicated at all. We just define a new view by creating a Python function and passing in a parameter called request. Next, we  return and render the template file we just created.

Then, the last step to make this work is to import the view to a file called "urls.py" inside the core app folder.

```
# add this line above the "urlpatterns" list
from blog.views import frontpage

# add this line inside the "urlpatterns" list
path('', frontpage, name='frontpage'),
```

First, we simply import the view we just created. Then we append the  view to a list of urls. The "''" is the address, then we pass in the  view and then we give it a name "frontpage". This makes it really easy  to reference diffrent places in our project.

If we now go to http://127.0.0.1 in our browser, we should see the front page we just created.

## List of blog posts

A static front page like we have now isn't exciting. We need to get  the blog posts from the database. To do this, we need to change the  "views.py" file inside the blog app again.

```
# add this line above the front page view
from .models import Post

# change the front page view like this
def frontpage(request):
	posts = Post.objects.all()

	return render(request, 'blog/frontpage.html', {'posts': posts})
```

It's not a big change, but it's enough to get all the blog posts from the database. First, we import the database model. Then we create a  lists of posts inside the view. This will get all the blog posts from  the database.

To access this list of posts in the template, we need to pass them in to the render function together with the template. "posts" will now be  available for us in the template.

Next, we need to do some changes to the front page template.

```
{% extends 'blog/base.html' %}

{% block content %}
	{% for post in posts %}
		<div class="post block">
			<h2 class="subtitle">{{ post.title }}</h2>

			<small>Posted at {{ post.date_added }}</small>

			<p>{{ post.intro }}</p>
		</div>
	{% endfor %}
{% endblock %}
```

Looping through a list of objects is really easy. To access the title and the other fields, we can just say "{{ post.title }}" and the  content of it will be printed there.

If you go back to the browser again and refresh, you should see a  simple list of the blog posts you added in the admin interface.

## Detail view of blog post

Having a list of blog posts isn't enough. We need to make it possible to click the posts so we can see all the details of it.

First, create a new file inside the "templates/blog" folder called "post_detail.html". It should look like this:

```
{% extends 'blog/base.html' %}

{% block content %}
	<h1 class="title">{{ post.title }}</h1>

	<small>Posted at {{ post.date_added }}</small>

	<p><strong>{{ post.intro }}</strong></p>

	<p>{{ post.body }}</p>
{% endblock %}
```

As you can see here, this template also extends the base template. We show the title, the date added and the text fields. I added an  <strong> element around the intro text to separate it from the  body text a little bit.

Now, we need a new view from this. This view can be added below the front page view.

```
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'blog/post_detail.html', {'post': post})
```

This view is similar to the front page, but we have one extra  parameter in the function. "slug" is the address to the blog post and we get this from the "urls.py" file. Inside the view, we get the post from the database based on the slug.

Next, we need to change the "urls.py" file so we can have a link to this view.

```
# append ", post_detail" 
from blog.views import frontpage, post_detail

# add at the bottom of the urlpatterns list
path('<slug:slug>/', post_detail, name='post_detail')
```

This is a dynamic path. The first "slug" tells Django that we expect  that the url should contain a slug. The second "slug" is the parameter  we pass into the post_detail view we just created.

Now, the last step to make this work is to add a read more button to the blog post list on the front page.

```
# add this line below the intro text
<a href="{% url 'post_detail' post.slug %}">Read more</a>
```

Here we use a function from Django called "url". We pass in the name  of the view we want to link to (post_detail) and then we add the slug to the post we want to visit. Django will automatically render the correct address for us now.

If you go to the browser now and refresh, you will see that we have a read more button and if you click it, you will see the detail view of a blog post.

We now have a very simple blog, but one this is missing and that is comments.

To store the comments, we will need a new database model. So below the "Post" model, add this:

```
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
```

- The "post" field is a reference to the post this comment belongs  to. The related_name option is the name of the index in the database,  this makes it easy to get the comments from the database. The on_delete  option makes sure that when we delete a post, the connected comments  will also be deleted.
- The four other fields is similar to the fields inside the post.

Since we have changed the models file, we need to update the database. Let's go to the command line and stop the web server.

To update the database, we run the same commands as earlier.

```
$ python manage.py makemigrations
$ python manage.py migrate
```

Great, let's create a form for the comments. I will begin by creating a new file called "forms.py" inside the blog folder.

```
from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'email', 'body']
```

This is a form type called ModelForm. This makes it really easy to  generate forms based on a database model. We pass in the model we want  to use and which fields. We need to add the "post" field manually and  "date_added" will be added automatically by Django.

To show this form on the detail page, we first need to add it to the view.

```
# import redirect together with render
from django.shortcuts import render, redirect

# add this line together with the other imports
from .forms import CommentForm

# change the post detail view
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
    	form = CommentForm(request.POST)

    	if form.is_valid():
    		comment = form.save(commit=False)
    		comment.post = post
    		comment.save()

    		return redirect('post_detail', slug=post.slug)
    else:
    	form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})
```

We have done a lot of changes here.

1. We import a new shortcut called "redirect".
2. We import the form we just created.
3. Inside the view, we check if the form is submitted by checking the request method.
4. If the form is submitted, we created an instance of it and pass in the post data.
5. Next, we check if the form data is valid.
6. If the form data is valid, we create a new "comment" object and  pass in the "commit=False" option. This is because this field is  required and the database would throw an error if we tried to save.
7. Next, we connect a post to the comment and save.
8. When the comment is added, we redirect the user back to the post.  We use the name of the view "post_detail" and pass in the slug.
9. If the request method isn't post, we just create an empty instance of the form.

The last step now is to show the form inside the template.

```
{% extends 'blog/base.html' %}

{% block content %}
	<h1 class="title">{{ post.title }}</h1>

	<small>Posted at {{ post.date_added }}</small>

	<p><strong>{{ post.intro }}</strong></p>

	<p>{{ post.body }}</p>

	<hr>

	<h2 class="subtitle">Add comment</h2>

	<form method="post" action=".">
		{% csrf_token %}

		{{ form.as_p }}

		<div class="field">
			<div class="control">
				<button class="button is-success">Submit</button>
			</div>
		</div>
	</form>
{% endblock %}
```

First we just create a simple form element. The first thing we add  inside this form is a tag from Django to generate a CSRF token. This is  some built in security to prevent XSS attacks.

There are several ways to present a form. The simplest is to just add {{ form.as_p }}, this will generate the form as paragraphs.

Now you can go to the browser to test this functionality.

The last step now is to display the comments above the comment form.

```
<p>{{ post.body }}</p>

<hr>

<h2 class="subtitle">Comments</h2>

{% for comment in post.comments.all %}
	<article class="media">
		<div class="media-content">
			<div class="content">
				<p>
					<strong>{{ comment.name }}</strong> <small>{{ comment.date_added|timesince }} ago</small>
					<br>
					{{ comment.body }}
				</p>
			</div>
		</div>
	</article>
{% empty %}
	<div class="notification">
		No comments yet...
	</div>
{% endfor %}

<hr>

<h2 class="subtitle">Add comment</h2>
```

To get all the comments beloning to a post we can just say  "post.comments.all". This is thanks to the related_name we added in the  database model. The comment consists of a name, date added and the body. To spice up the date added a little bit, we pass in the value to a  Django filter called "timesince". This will convert the date to a cooler format like "50 minutes ago" and similar.

## Video version of this post



## Summary

​	And that's it for this tutorial. I hope you liked it. I would really  appreciate it if you shared this article with your friends. If you have  any questions about the content here, feel free to leave a comment  below. 

​          

## video :

https://www.youtube.com/watch?v=m3hhLE1KR5Q&feature=emb_title