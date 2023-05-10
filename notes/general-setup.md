
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
