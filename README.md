# MedicalNER
MedicalNER which can extract medicine from a given text and then fetch its information from the database
## Follow the steps below to run the application

install postgreSQL as DataBase
configure the database in the settings

### Steps

1. Extract the Project folder (MedicalNER)
2. Change directory to the extracted folder
```
    $ cd MedicalNER
```
3. create a python vertual environment
```
    $ python -m venv venv
```
4. Activate the vertual environment
```
    $ venv/Scripts/activate.bat
```
5. install all the project dependancies
```
    $ pip install -r requirements.txt
```
6. configure database in settings.py file
```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'medicalner',
            'USER': 'postgres',
            'PASSWORD': 'admin',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }
```
7. Run Migration commands
```
    $ python manage.py makemigrations
    $ python manage.py migrate
```
8. Run populate.py script file to load the data into database
```
    $ python populate.py
```
9. create superuser for admin site
```
    $ python manage.py createsuperuser
```
10. Start / run the server
```
    $ python manage.py runserver
```
11. Use the url to check the functionality
```
    http://127.0.0.1:8000/search/
```
