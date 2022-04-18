# ABOUT:  `cityparkcollector`

Goal: give users a place to record their visits to parks in their city, with a mind towards accessibility and community building. The available resources would be the focus in a social-media/sharing aspect. 

## To get started coding in this project:

* Activate the virtual environment
```bash
cd cityparkcollector
source .env/bin/activaate
```

* Install the dependencies for this project:
```bash
pip3 install requirements.txt
```

* Confirm database exists and connect
```bash
psql cityparkcollector
```
*if there's an error, enter psql shell and run:*
```sql
CREATE DATABASE cityparkcollector;
\c cityparkcollector
```

* Run the server
```bash
python3 manage.py runserver
```

* Make and Migrate dcb changes
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```


ERRORS:
* photo upload

CSS:
* park detail page (margin, padding)
* nav bar in a row
