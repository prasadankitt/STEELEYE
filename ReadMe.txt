So for making API using Rest we have to do these set up before

1. created a folder (STEELEYEASSIGNMENT),enter into it (cd STEELEYEASSIGNMENT),install django (pip install django)
2. start our project(API) by command "django-admin startproject API"
3. install django rest framework in it by command "pip install djangorestframework"

Now we are ready to move forward our project is started.

-> make "views.py" file in our project.
  where we define our views to do task of user whether it is of POST or GET
To check follow path : API/views.py
  
-> now go to "urls.py" and include our class based view that is Testview and also in django we have to tell django about 
    rest framework so include a path for it too .
To check follow path : API/urls.py    

-> In "settings.py" we have to add django restframework in our installed app section
To check follow path : API/settings.py


-> Now we use serializers to give structure recieve or give data into json format
-> so create a app named SteelAPI in our project as we have to create model and use serializers
    "python manage.py startapp SteelAPI"  and in "settings.py" file add our app in installed app section
To check follow path : API/settings.py    

-> Define our schema in "models.py" file , after creating schema we have to makemigrations to database
   so we use "python manage.py makemigrations" and then "python manage.py migrate" and it will migrate my tbles or models we created
To check follow path : SteelAPI/models.py

-> Register our model in "admin.py" file
To check follow path : SteelAPI/admin.py

-> now in our "serializers.py" file we specify fields to configure in our API
To check follow path : SteelAPI/serializers.py

-> now our API is available so runserver on our local host by "python manage.py runserver"

-> create superuser to login
-> now using postman we can verify our API by choosing Get option there and get all the data present in our database
   by choosing  Post option we can add data
   and see the changes in our database 

Please check Screenshots pdf.