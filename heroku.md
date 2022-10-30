* install python (look for the determined version in docs) locally

* install postgres locally   (https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart)

* install cli (command line interface) to manage herouku through terminal :

  ​	sudo snap install heroku --classic

* add requirements.txt file in src folder :

  ​	pip freeze >requirements.txt

* make folder with any name like deployment in home (just for organization) then create a folder with a name that represent the project name (like labanco)

* next step is taking a copy of our project  to deal with it out from the base project (to get away from errors ) and pushing it to git hub to and deploy it .

  * take a copy of the content of src folder and past it to labanco  folder 

  * make sure that requirements.txt and is copied also .

  * go to labanco folder and initialize git :

    ​	git init

  * go to labanco and create virtualenv:

    ​	python3 -m virtualenv env

    ​	source env/bin/activate

  * install requirements file content:

    ​	pip install -r requirements.txt

  * git status

  * before adding to staging area make .gitignore file in src folder.

  * add .gitignore file on src folder and put this on it :

    ```
    # Byte-compiled / optimized / DLL files
    __pycache__/
    *.py[cod]
    *$py.class
    
    # C extensions
    *.so
    
    # Distribution / packaging
    .Python
    build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    share/python-wheels/
    *.egg-info/
    .installed.cfg
    *.egg
    MANIFEST
    
    # PyInstaller
    #  Usually these files are written by a python script from a template
    #  before PyInstaller builds the exe, so as to inject date/other infos into it.
    *.manifest
    *.spec
    
    # Installer logs
    pip-log.txt
    pip-delete-this-directory.txt
    
    # Unit test / coverage reports
    htmlcov/
    .tox/
    .nox/
    .coverage
    .coverage.*
    .cache
    nosetests.xml
    coverage.xml
    *.cover
    *.py,cover
    .hypothesis/
    .pytest_cache/
    cover/
    
    # Translations
    *.mo
    *.pot
    
    # Django stuff:
    *.log
    local_settings.py
    db.sqlite3
    db.sqlite3-journal
    
    # Flask stuff:
    instance/
    .webassets-cache
    
    # Scrapy stuff:
    .scrapy
    
    # Sphinx documentation
    docs/_build/
    
    # PyBuilder
    .pybuilder/
    target/
    
    # Jupyter Notebook
    .ipynb_checkpoints
    
    # IPython
    profile_default/
    ipython_config.py
    
    # pyenv
    #   For a library or package, you might want to ignore these files since the code is
    #   intended to run in multiple environments; otherwise, check them in:
    # .python-version
    
    # pipenv
    #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
    #   However, in case of collaboration, if having platform-specific dependencies or dependencies
    #   having no cross-platform support, pipenv may install dependencies that don't work, or not
    #   install all needed dependencies.
    #Pipfile.lock
    
    # poetry
    #   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
    #   This is especially recommended for binary packages to ensure reproducibility, and is more
    #   commonly ignored for libraries.
    #   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
    #poetry.lock
    
    # pdm
    #   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
    #pdm.lock
    #   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
    #   in version control.
    #   https://pdm.fming.dev/#use-with-ide
    .pdm.toml
    
    # PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
    __pypackages__/
    
    # Celery stuff
    celerybeat-schedule
    celerybeat.pid
    
    # SageMath parsed files
    *.sage.py
    
    # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/
    
    # Spyder project settings
    .spyderproject
    .spyproject
    
    # Rope project settings
    .ropeproject
    
    # mkdocs documentation
    /site
    
    # mypy
    .mypy_cache/
    .dmypy.json
    dmypy.json
    
    # Pyre type checker
    .pyre/
    
    # pytype static type analyzer
    .pytype/
    
    # Cython debug symbols
    cython_debug/
    
    # PyCharm
    #  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
    #  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
    #  and can be added to the global gitignore or merged into this file.  For a more nuclear
    #  option (not recommended) you can uncomment the following to ignore the entire idea folder.
    #.idea/
    
    ```

    

  * git add .

  * git commit -m"initial commit"

  * pip install gunicorn

  * pip freeze > requirements.txt

  * create new file in src with name Procfile (to manage wsgi) and write on it :
	  don;t forget to replace project wit your project name

    ```
    web: gunicorn project.wsgi
    ```

    (project is the name of your project)

  * git add .

  * git commit -m"add Procfile and install gunicorn"

  * pip install django-heroku

  * if some error happened ,type this :

    ​	sudo apt-get install libpq-dev

  * pip freeze > requirements.txt

  * in settings.py :

    ​	in first line :

    ​		import django_heroku

    ​	in last line:

    ​		django_heroku.settings(locals())

    ​	in MIDDLEWARE add this line (to manage static files problems) : 

    ​		'whitenoise.middleware.WhiteNoiseMiddleware',

    ​	static files settings :

    ​		STATIC_URL = '/static/'

    ​		STATICFILES_DIRS = [

    ​	    BASE_DIR / "static",

      	  '/var/www/static/',

    ​		]

    ​	add after them :

    ​		STATICfILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

  * to change the secrete key in settings do this in terminal (in the same place you are (in labanco in terminal that is activated)):

    * python (to open python)
    * import secrets
    * secrets.token_hex(24).title()
    * it will generate a key so copy it and put it instead of the one in settings.py

  * let DEBUG = True (don't change it because heroku will sleep the website after 30 minutes of not using so the static files will be not working if DEBUG = False)

  * come back to terminal and go out python by exit

  * write this un terminal:
	  heroku login

  * press any key to open the browser

  * then login : 

    * withallah010951@gmail.com
    * withALLAH010*#

  * come back to terminal after logging in the browser , you will find your self logined to heroku in terminal too.

  * create app in heroku : with name (labanco)

    * heroku create labanco 

  * heroku will create the app and give you two links

    * https://labanco.herokuapp.com/   (link of our website)
    *  https://git.heroku.com/labanco.git (link for remote reposetory)
    * to open this website :
      * heroku open

  * to link between the local stage and remote stage git :

    * ```
      heroku git:remote -a labanco
      ```

      **to get this line**

      1- go to your heroku dashboard 
      2- select deploy
      3- you will find it at end of the page

  * git remote -v (just to check that the connection between local and remote stage is done)

  * git add . 

  * git commit -m"dfgsdf"

  * git push heroku master

  * heroku open

  * to correct database error:

    ​	heroku run python manage.py migrate

  * heroku restart

  * heroku open

  * heroku run python manage.py createsuperuser

  * heroku config:set DISABLE_COLLECTSTATIC=1

  * in settings.py , update ALLOWED_HOSTS = []  to be :

    ALLOWED_HOSTS = ['https://labanco.herokuapp.com/']