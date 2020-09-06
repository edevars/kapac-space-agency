# KAPA-C | Space Travel Agency

![Kapa-c](./assets/banner.png)
#### A fiction project to learn Django creating a web app that controls all the travels from *KAPA-C*, the best travel agency in the galaxy!

---
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