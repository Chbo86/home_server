# Allgemeine Information
    Aufnahme Programm ( ActivePresenter )
    mwc ( Model View Controller)
    clockify ( F1 = Start - Tracking )

## Anforderung Programme

### Minimal:
x   1. Internet
x   2. Aktuelle Python Version (3.6, 3.7 oder 3.8) – V3.8.4 https://www.python.org/ftp/python/3.8.4/python-3.8.4-amd64.exe
x   3. Python und pip in Path (python -V und pip -V sollten funktionieren)
x   4. Visual Studio Code mit folgenden Paketen (Extensions)
x       1. Python V2020.6.9.1350 https://marketplace.visualstudio.com/items?itemName=ms-python.python
x       2. Django (Baptiste Darthenay) V0.20.0  https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django

### Optional:
x   1.  Git und GitBash (https://git-scm.com/)
x   2.  Visual Studio Code mit folgenden Paketen
x       1.  Bracket Pair Colorizer 2 V0.2.0 https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2
x       2.  German Language Pack V1.47.3 https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-de
x       3.  Prettier V5.1.3 https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode
x       4.  VS Icons V10.2.0 https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons
x       5.  Git Graph https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph

## Ablauf

### Ordnerstruktur
    1. Neuen Ordner Erstellen z.B.: ( C:\coding\tutorial )
    2. Rechte Maustaste -> Git Bash Here ( Erstellen der git init )

### git bash
    1. gitignore hinterlegen https://www.toptal.com/developers/gitignore/api/windows,visualstudiocode,django,python
    2. git clone url
        1. goto Virtualenv erstellen ( 2. )
        2. goto Virtualenv aktivieren und starten ( 1. o. 2.)
        3. goto Virtualenv ( Backup & install pakete ) ( 3. )
        4. goto Virtualenv aktivieren und starten ( 3. )
        5. Django ( ab 3. )
    3. git bash
        Start . ( Windows Explorer "Projekt" starten )
        code . ( Visual Studio Code starten)

### Virtualenv erstellen
    1. pip install virtualenv
    2. python -m virtualenv venv

### Virtualenv aktivieren und starten
    1. source venv/Scripts/activate ( venv Aktivieren ) ( Linux )
    2. venv\Scripts\activate ( venv Aktivieren ) ( Windows CMD )
    3. Django starten
        1. CD Projekt ( Name )
        2. python manage.py runserver ( Django Server starten ) ( Global )
        3. python manage.py runserver 0.0.0.0:8000 ( Django Server starten ) ( Öffentlich )

### Virtualenv ( Backup & install pakete )
    1. pip freeze ( pakete initialisieren )
    2. pip freeze > requrements.txt ( Auflistung der Installierten Pakete in der requrements.txt )
    3. pip install -r requrements.txt ( Installieren der Aufgelisteten Pakete aus der requrements.txt )

### Django
    1. pip install django
    2. django-damin startproject name ( Projekt erstellen )
    3. python manage.py makemigrations ( Datenbank Initialisieren )
    4. python manage.py migrate ( Datenbank intigrieren )
    5. python manage.py createsuperuser ( Admin - Bereich )
        1. winpty python manage.py createsuperuser ( Passwort zurücksetzen )
    6. python manage.py startapp name ( APP ( Funktion ) erstellen )

### Projekt Name Urls
    1. urlpatterns
        1. Einpflegen der APP z.B.: ( path('simple/', simpleView), ) wenn ( Öffentliche Funktion )

### Settings
    1. INSTALLED_APPS
        2. #myApps ( Einpflegen der APP ) z.B.: ( 'products', )
    2. ALLOWED_HOSTS = ['*'] ( Netzwerkeinstellung ) ( Freigabe alle hosts )
    3. 'DIRS': [os.path.join(BASE_DIR, "templates")],
    4. NAV Database ( https://pypi.org/project/django-mssql-backend/ )
        #NAV Database ( MS SQL )
        # pip install pyodbc
        # pip install django-mssql-backend 
        #import pyodbc
        # 'xxx':  {
        # 'ENGINE': 'sql_server.pyodbc',
        #    'NAME': 'xxx',
        #    'HOST': 'XXX.XXX.XXX.XXX',
        #    'PORT': '',
        #    'USER': 'XXXX',
        #    'PASSWORD': 'XXXXXX',
        #    'OPTIONS': {
        #         'driver': 'ODBC Driver 13 for SQL Server',
        #     },
        # },

### inspectdb
    1.  python manage.py inspectdb --database=interhydraulik "Interhydraulik%item" > item.py
        python manage.py inspectdb --database=interhydraulik "IH_View_Prod_Order_Line_Search" > IH_View_Prod_Order_Line_Search.py
        IH_View_Prod_Order_Routing_Line_2
    2.  python manage.py makemigrations ( Datenbank Initialisieren )
    3.  python manage.py migrate ( Datenbank intigrieren )
    4.  python manage.py migrate --run-syncdb

### Chart
    1.  pip install django-chartjs ( https://pypi.org/project/django-chartjs/ )

## Wichtige Dateien
    1. views.py ( APP Ordner )
    2. models.py ( APP Ordner )
    3. urls.py ( Projekt Ordner )
    4. settings.py ( Projekt Ordner )
    5. admin.py ( Projekt Ordner )
