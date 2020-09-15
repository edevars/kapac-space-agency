# KAPA-C | Space Travel Agency

![Kapa-c](./assets/banner.png)
#### A fiction project to learn Django creating a web app that controls all the travels from *KAPA-C*, the best travel agency in the galaxy!

---

## The magic of the Django ORM

If you are familiarized with the creation of web apps, you know that the configuration of a database is essential for big projects. Depending on which database you choose the backend implementation could be different, but the commons steps are that you need to set up the drivers to connect to the database and create the methods to do CRUD operations. 

In some frameworks exists the concept of ORM (Object Relation Mapper). This thing helps you to forget all that hard set up and only worry about you to create the models of your entities. Another big advantage is that the ORM let us to abstract all the logic of the creation of tables in the different relational database management systems (a.k.a RDBMS) like PostgreSQL or MySQL. 

> Note: Django can also work with No SQL databases like MongoDB

By Default Django use SQLite as a predefined database because it doesn't need to use another dependency to work with Python. Obviously, in production environments, this isn't a good practice. 

### Space Travel Agency | ER Model

This is a basic diagram of the entities of our database. We have Travels, space ships, different kinds of seats, tickets and users.

![Space Travel Agency](https://i.imgur.com/hrQpqdn.png)

### Understanding what is a Model

The models in Django have all the information about your data. They contain the fields and data types that are inserted as tables in the database, but all that process is handled by the Django ORM, its easy to work in this way. They are represented as a class in the code. 

### Creating our models

To start we are going to create the models of the travel app. 

> Remember, apps in Django are a kind of modules of your application. These can be used in other Django projects.

To do this, in the `Travel` app we have a file named `models.py`, inside of this we can write the specification of each model. Django includes a lot of data type fields to describe all the fields of the entities in our database. You can check all these data types [here](https://docs.djangoproject.com/en/3.1/ref/models/fields/).

First specify the `Travel` model:

```python
    class Travel(models.Model):
        destination = models.CharField(max_length=200)
        arrival_time = models.DateTimeField()
        departure_time = models.DateTimeField()
        image = models.ImageField()
```

As you can see, we use a special type field called `ImageField`. This data field will help us later to upload images in our application, in combination with the dependency `pillow`. We will configure this later. 

To apply this model to our database we need to understand a new concept, migrations. 

## Migrations in Django 

Migrations are the way to propagate the changes in your models into the schema of your database. As simple as that. 🥳

To apply the `Travel` model to the schema we need to run the command `makemigrations` specifying our app. 

```bash
python manage.py makemigrations travels
```

Buy then you are going to see this error in the console. 

![makemigrations_fail](./assets/makemigrations.png)

So... to fix this we need to install the `travels` app in the Django project. This is really simple, go inside the main `space_agency` folder and look for the `settings.py` file. Go directly to this line: 

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

and then add the name of the app that you want to install. In our case is the `travels` app.

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # adding the travels app
    'travels' 
]
```

Now, try to execute the `makemigrations` command again. If all was ok, you see a message like this in your terminal. 

```bash
python manage.py makemigrations travels
```

![makemigrations_fail](./assets/makemigrations_ok.png)

if you look inside of your project, you have a new file inside in the migrations folder. This file is generated automatically by Django whenever you do a modification to your models. 

But this isn't all, you need to apply this migration to your project. To do this only execute the command 'migrate' with the manager of Django. 

```bash
python manage.py migrate
```

With this you have been applied all the changes to your database, no matters if is SQLite or PostgreSQL, this is the magic of behind Django ORM. 