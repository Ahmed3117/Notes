​    

## use Django on a DigitalOcean droplet :

I use DigitalOcean for all of my projects, Code With  Stein as well. DigitalOcean is cheap, good servers and a easy to use  control panel.            

### Setting up the environment

When I have set up our droplet using DigitalOcean's control panel is to update everything so I know everything is OK.

```
$ sudo apt-get update
$ sudo apt-get upgrade
```

I like to create a user and a group to handle everything there so  that the root user is not involved with my project. Lets add the user,  group and it's home folder

```
$ sudo groupadd --system djangoapps
$ sudo useradd --system --gid djangoapps --shell /bin/bash --home /djangoapps/codewithstein djangouser
$ sudo mkdir -p /djangoapps/codewithstein/
$ sudo chown djangouser /djangoapps/codewithstein/
```

I feel that it's important to separate the python packages used in  our project from the global ones and that is done by using a virtual  environment (virtualenv).

```
$ sudo apt-get install python-virtualenv
```

Now that the virtualenv is installed I switch over to the newly  created user so everything with permissions is handled correctly.

```
$ sudo su - djangouser
$ cd /djangoapps/codewithstein/
$ virtualenv .
$ source bin/activate
```

The environment is now created and activated. Packages we install  using pip will only be activated for our virtual environment. Let's  intall django and create our project.

```
$ pip install django
$ django-admin.py startproject codewithstein
$ cd codewithstein
```

### Gunicorn

Django's built in single-threaded development server shouldn't be  used in production. So we use Gunicorn instead which is perfect for the  task.

```
$ pip install gunicorn

# Let's test it

$ gunicorn codewithstein.wsgi:application --bind codewithstein.com:8001
```

\# Open codewithstein.com:8001 in the browser to check that everything is running

I need to set up the gunicorn config file. Here is an example of how it could look like:

```
#!/bin/bash

NAME="codewithstein"
DJANGODIR=/djangoapps/codewithstein/codewithstein
SOCKFILE=/djangoapps/codewithstein/run/gunicorn.sock
USER=djangouser
GROUP=djangoapps
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=codewithstein.settings
DJANGO_WSGI_MODULE=codewithstein.wsgi

# Activate the virtualenv
cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
```

The last gunicorn'y thing I do is to make the config file runable.

```
$ sudo chmod u+x bin/gunicorn_start
```

### Supervisor

To make sure that my django project is always running and started  automatically if the server is rebooted I use Supervisor. I install it  using the following command:

```
$ sudo apt-get install supervisor
```

I create a new config file inside /etc/supervisor/conf.d/ called codewithstein.conf and write the following options.

```
[program:codewithstein]
command = /djangoapps/codewithstein/bin/gunicorn_start; Start the app
user = djangouser; Tell which user to use
stdout_logfile = /djangoapps/codewithstein/logs/gunicorn_supervisor.log; Log file
redirect_stderr = true
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8; Set encoding to UTF-8
```

A couple of more steps left to make supervisor work:

```
$ sudo supervisorctl reread # Make supervisor read the config
$ sudo supervisorctl update # Update supervisors config
$ sudo supervisorctl status # Check that the django app is running
```

### Nginx

Nginx is used for proxy forwarding the traffic to the gunicorn and to serve media files for our project. This is something that Nginx does  perfectly. Install Nginx by running sudo apt-get install nginx.

When Nginx is installed I create a new config file inside the  /etc/nginx/sites-availeable called codewithstein. Here is an example of a config.

```
upstream codewithstein_server {
    server unix:/djangoapps/codewithstein/run/gunicorn.sock fail_timeout=0;
}

server {
    listen 80;
    server_name codewithstein.com;

    client_max_body_size 4G;

    access_log /djangoapps/codewithstein/logs/nginx-access.log;
    error_log /djangoapps/codewithstein/logs/nginx-error.log;
 
    location /static/ {
        alias /djangoapps/codewithstein/static/;
    }
    
    location /media/ {
        alias /djangoapps/codewithstein/media/;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;

        if (!-f $request_filename) {
            proxy_pass http://codewithstein_server;
            break;
        }
    }

    # Error
    
    error_page 500 502 503 504 /500.html;
    location = /500.html {
        root /djangoapps/codewithstein/static/;
    }
}
```

Last part of the Nginx set up is to create a symbolic link to add the page to Nginx's enabled pages and then restart Nginx.

```
$ sudo ln -s /etc/nginx/sites-available/codewithstein /etc/nginx/sites-enabled/codewithstein
$ sudo service nginx restart
```

Everything should be ready for you to now open the url you set in  "server_name". If anything here was unclear you're free to add a comment and ask me anything :-)

### Multiple sites

If you have want to host multiple sites on your droplet there is  nothing wrong with that. Just go back up again to where we created our  first virtual environment and go through the guide again and just change codewithstein or whatever your site name is with the new one.

### SSL using Let's encrypt

Adding a SSL certificate to you Django sites is well documented many  places. Instead of me writing a duplicate of this I'm adding a link here  (https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04). This is a guide I often use when adding SSL to my sites.

### Try DigitalOcean your self

If you go to [DigitalOcean](https://m.do.co/c/d3cdd4293e67) using this link you will receive a $10 credit. So you'll be able to test their cheapest droplet for two months!

