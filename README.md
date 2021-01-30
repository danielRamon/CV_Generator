# CV_Generator
This program has the purpose of being able to generate a web curriculum vitae through the simplicity of Django. It is based on python and makes use of its basic libraries. On the other hand, for the frontend, it is mostly based on bootstrap 4.

### Getting started

1. Download or clone the proyect. 
2. Make a migration and migrate the data base currently configured with SQLite. Go to  the directory proyect and execute this commands in orde to create the structure db.
   	python manage.py makemigrations
   	python manage.py migrate

3. Create superuser to manage your admin django. Execute the command and follow the prompt instructions.
`python manage.py createsuperuser`

4. Run the server DJango
`python manage.py runserver`

5. Access the DJango administrator with the created user and the link obtained after starting the DJango server.
`https://[Django-url]/admin`

6. Create the django models beginning with Identity.

7. Enjoy your web curriculum accesing the following url in your django.
`https://[Django-url]/curriculum/[your-vat]`
