# Module 12 - Python Django - eindopdracht voorbeeld

## Installatie:

### clone de repo
```
git clone https://github.com/ttijs/module-12-Django-project
```

### cd in de nieuw aangemaakte map
```
cd module-12-Django-project/
```

### maak een virtual environment aan met de naam venv
```
virtualenv venv
```

### activeer de virtual env
```
# git bash
source ./venv/Scripts/activate
# cmd of Powersheel
.\venv\Scripts\activate
# OSX
source ./venv/bin/activate
```

### installeer de benodigde modules
```
pip install -r requirements.txt
```

### make de databaseschema aan op basis van de models
```
python manage.py migrate
```

### maak een user aan
```
python manage.py createsuperuser
```

### start de server
```
python manage.py runserver
```

### en ga naar /admin om items toe te voegen
