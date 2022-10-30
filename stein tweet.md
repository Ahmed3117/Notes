​    

[codewithstein.com](https://codewithstein.com/how-to-tweet-using-django/)

# How To Tweet Using Django | Code With Stein

Code With Stein

3 minutes

------

​                Learn how to use a Python library called Tweepy to post tweets to your timeline using Django.            

I just installed Django and created an empty project. Feel free to use an existing project if you want to do that.

Now it's time to show you how to use a library called tweepy to tweet using Django. First, we can install the library by running "pip install tweepy".

To use the twitter api, you need some credentials from twitter. Go to [developer.twitter.com](https://developer.twitter.com/). Here you need to create an app in order to get the credentials you need. When you're ready, you can continue.

I'm going to create a django app which will be used for tweeting.

```
$ python manage.py startapp post
```

Let's register this in the settings.py file so django knows we will be using it

```
INSTALLED_APPS = [
...
'post',
...
```

Let's create a view which can be used for this:

```
def index(request):
	if request.method == 'POST':
		content = request.POST.get('content', '')

		if content:
			print('Content:', content)

			return redirect('post')

	return render(request, 'post/index.html')
```

And then a simple template:

```
<form method="post" action=".">
	{% csrf_token %}

	<input type="text" name="content"><br>

	<button>Submit</button>
</form>
```

Then we just need to add this to the urls, and we can test it.

```
from post import views

urlpatterns = [
    ...
    path('', views.index, name='index')
]
```

If you open up the browser now and submit the form, you would see the contents in the terminal.

## Using Tweepy

First, I want to define the api credentials in the settings.py file:

```
# Twitter

API_KEY = 'ruQWMpxFBziKs08KlVrpVsACn'

API_KEY_SECRET = 'IRruQCLI4w6RlWNxW6Iw6Djjq4DBmhOeO1O3iYwhaW5Tg5RFoK'

ACCESS_TOKEN = '1006977823687479297-AoHcTmvEyXYyUUNveTOeKm6IQo0Y1t'

ACCESS_TOKEN_SECRET = '0OlSB5xjPbn6O0HSXTJzazWBbQHdux1NZuOqIxFCF9BF1'
```

Then we need to import two new things in the views.py file:

```
import tweepy

from django.conf import settings
```

If we now just alter the view a little bit, the backend will be ready for tweeting:

```
if content:
	print('Content:', content)

	auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
	auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

	api = tweepy.API(auth)
	api.update_status(content)

	return redirect('post')
```

## Video

​         https://www.youtube.com/watch?v=4F8oKSStRfQ