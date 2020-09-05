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
