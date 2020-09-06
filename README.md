# KAPA-C | Space Travel Agency

![Kapa-c](./assets/banner.png)
#### A fiction project to learn Django creating a web app that controls all the travels from *KAPA-C*, the best travel agency in the galaxy!

---
### Start a Django project
Before we start coding and building the site for the best space travel agency, we need to setup all our enviroment. To do this we need to install the latest version of Django. I recommend you use a virtual enviroment. In my case I'm going to use conda as default package manager, but you can use pip if you prefer.

**Creating a virtual env**
```bash
conda create -n space_agency
```
and then
```bash
conda activate space_agency
```
**Installing Django**
```bash
conda install -c conda-forge django
```
**Creating a new Django project**
A Django project is a web aplication that do something in general, for example a blog, a news site, a social network, etc. To create this project we have to execute the next command.
```
django-admin startproject space_agency 
```

In this case `space_agency` is the name of our project. This command generates the next folders and files structure:
```
space_agency
    ├── manage.py
    └── space_agency
        ├── asgi.py
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
``` 

These files are:

- The outer **space_agency/** root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
- **manage.py:** A command-line utility that lets you interact with this Django project in various ways. 
- The inner **space_agency/** directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. space_agency.urls).
- **space_agency/__init__.py:** An empty file that tells Python that this directory should be considered a Python package.
- **space_agency/settings.py:** Settings/configuration for this Django project. 
- **space_agency/urls.py:** The URL declarations for this Django project; a “table of contents” of your Django-powered site. 
- **space_agency/asgi.py:** An entry-point for ASGI-compatible web servers to serve your project. 
- **space_agency/wsgi.py:** An entry-point for WSGI-compatible web servers to serve your project. 

With this you have now a Django project initialized to create some apps inside.


### Development server
So we have all the setup of our project. If you can test that all the configuration works, run the manage.py script with the next instruction:
```bash
python manage.py runserver
```
This instruction runs the development server of our project. It's a light version of our web app that let us see the changes in our web pages in real time. 

To run in a specific port you can execute the command with an extra parameter. For example, if we can run our project in the port **3000**, we have to execute the next instruction: 
```bash
python manage.py runserver 3000
```

In both cases we are going to have the next output in the terminal:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 05, 2020 - 23:22:45
Django version 3.1.1, using settings 'space_agency.settings'
Starting development server at http://127.0.0.1:3000/
Quit the server with CONTROL-C.

```

> ⚠ Remember activate your virtual environment and be inside the outer `space_agency` directory

Dont't worry about the migrations warning. This is an importatn concept in Django but we will see them later.  

If you click in the URL of the development server you can see something like this in your browser:

![first page project](./assets/dev_server_project.png)

*The rocket in this page it's a mere coincidence*

### Creating our first app

In this moment it's posible that you think that a project and an application it's the same, but the reality is that this isn't true.

In the docs of Django says:
> An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

Clear enough, right? So, if you understood this we can continue creating our first app. We can create the travels app, to do this we run the next command:

```bash
python manage.py startapp travels
```
This creates a new directory **travels** that has this structure:
 ```
 travels
├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
 ```
 This folder contains all the files of our travels app following the MTV pattern. 

 ### MTV Pattern

 The MTV Pattern is an important concept in Django. This a variation of the MVC pattern viewed in other languages like PHP. 

 ![MTV Pattern](./assets/MTV.png)
### Creating our first view

Views are python functions that take a web request and returns a web response. To create a view we can send an HTTP response in our travels app, for this we are going to use the `views.py` file.

**views.py**
```python
from django.http import HttpResponse 

def home(request): 
    dummy_html = "<h1> Hi! You are visiting the space travel agency</h1>"

    return HttpResponse(dummy_html)
```

This is a very basic view function, only lets us choose how we want to handle the data that is showing in the browser. To connect this response with a specific path or URL inside of our project, we need to create a `urls.py` file inside the travels app. This file configures which views you want to show in each URL. 

```python
from django.urls import path

from travels import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

All the views that you declare inside of `urlpatterns` are going to live under a specific URL associated with the project. For this, we need to go inside of the `space_agency` directory and configure the news URLs from the travels app. 

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    '''Adding the urls inside of the travels app'''
    path('travels/', include('travels.urls'))
]
```

Now, if you go to `http://127.0.0.1:8000/travels/` you can see the message created in your travels view.
![view response](./assets/first_view_capture.png)