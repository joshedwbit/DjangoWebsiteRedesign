
# setup
to start, drag whole project folder to vscode
to create a new app 'python manage.py startapp [appname]'

creating db tables, run 'python manage.py makemigrations, python manage.py migrate'
'python manage.py createsuperuser' = create super user

to run VM; python manage.py runserver inside the project directory ALTERNATIVELY use debugger

there is a main urls.py in project folder, but also inside each app = keeps app urls local to the app
	-acts as a controller = routes to specific views.py which routes to html (held in templates folder)

CSS/JS are held in a static directory - referenced at top of any template (html file) in same way a stylesheet is referenced

whenver a model is created it must be added to admin.py


# to pull in required packages: pip3 install -r requirements.txt

*** need to restart local environment if making config changes ***



similarities to D3R
apps = MVC build - can be used in multiple projects - therefore easier to replicate in Django
urls.py = controller + almost acts as provider too
requirements.txt = package.json lists dependencies


# standard practise
Standard practise:
create a requirements.txt file = saves project dependencies
running django file downloaded from web:
pip install -r requirements.txt
to install dependencies



1.
new app
added to settings.py
create urls.py inside app
pulled app urls.py into main urls.py
defined views (class based) and locations in views.py
inside settings.py of main, include staticfiles_dirs to reference additional static folders


2.
install sass
	1. pip install django-sass-processor
	2. add to installed apps in settings.py
	3. STATICFILES_FINDERS = [    'django.contrib.staticfiles.finders.FileSystemFinder',    'django.contrib.staticfiles.finders.AppDirectoriesFinder',    'sass_processor.finders.CssFinder',]
	4. create static/scss
	5. rather than load static, load sass_tags and change {% static to {% sass_src

pip install libsass
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
python manage.py collectstatic

initialise git repo
setup gitignore
pip freeze > requirements.txt = loads requirements.txt file


3.
admin
python manage.py createsuperuser
can then use these credentials to login to admin portal

how to setup a user login system on my django project, explain each step in detail



4.
database

python manage.py makemigrations
python manage.py migrate

once model is created inside the app models.py, will need to register the model in the app admin.py;
from .models import [tablename]

admin.site.register([tablename])

can populate via the admin portal

to display the model in a view, in views.py; from .models import [tablename]
inject into view

can use |safe filter to print html directly


5.
extends templates

6.
pip install libsass
python manage.py collectstatic
pip freeze > requirements.txt


7.
create new app
edit views
create + edit urls
create new templates folder with the right setup
create new static folder with the right setup

tweak main urls.py - add path
tweak main settings.py - add to installed apps + staticfiles_dirs add stylesheet

update styles.scss to pull in new styles (if necessary)

8.
If adding specific stylesheet/js to a view file, must include {% load sass_tags %}
at the top of the file
