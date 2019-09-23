# Scaffold Template

## *** Please clone this repository and do not directly make changes to it ***
### This is our boilerplate code for all apps we produce.
### It helps speed up development time and allow us to spend time focusing on the custom business logic.

<hr>

A few steps are needed before the boilerplate functions properly.

## app.py: Change both to project name

```PYTHON
# Change 'web' to project name.
web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'web')

# Change 'PROJECT' to project name.
app = Flask('PROJECT', root_path=web_dir)
```
<br>
<hr>

## .env: Configure DATABASE_URL

```PYTHON
DATABASE_URL="postgres://localhost:5432/postgres_server_name" # Change to your DB Name
```

###  Then add .env to .gitignore file (not added by default)

<br>
<hr>

## Install standard packages and dependencies

```PYTHON
pip install -r requirements.txt
```
This installs 25 commonly used packages and dependencies:

```PYTHON
boto3==1.9.130
botocore==1.12.130
certifi==2019.3.9
Click==7.0
colorama==0.4.1
docutils==0.14
Flask==1.0.2
Flask-Assets==0.12
Flask-Login==0.4.1
Flask-WTF==0.14.2
itsdangerous==1.1.0
Jinja2==2.10
jmespath==0.9.4
MarkupSafe==1.1.1
peewee==3.9.3
peewee-db-evolve==3.7.0
psycopg2-binary==2.7.7
python-dateutil==2.8.0
python-dotenv==0.10.1
s3transfer==0.2.0
six==1.12.0
urllib3==1.24.1
webassets==0.12.1
Werkzeug==0.15.1
WTForms==2.2.1
```

<br>
<hr>

## server.py: change import name to match project-name folder. i.e. nextagram_web

```PYTHON
import web #<---
```

<br>
<hr>

## Create a PostgreSQL database.

In Terminal:
```PYTHON
createdb project_name_dev
```

<br>
<hr>

## Create a virtual environment (always be in your virtualenv):

In Terminal:
```PYTHON
conda create -n project_name python=3.7
conda activate project_name
```

<br>
<hr>

## instead of typing python migrate.py everytime, run this command to type only 'migrate' in terminal to run it:

```PYTHON
echo -e '\nalias migrate="python migrate.py"\n' >> ~/.bash_profile
```

<br>
<hr>

## Build something cool!
```PYTHON
flask run
```
 
