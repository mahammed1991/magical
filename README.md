##########################################################################################################

# Project's README
Python Verssion Python 2.7.10 (default, Oct 14 2015, 16:09:02)

A simple Django Based Application to store companies and employees and Job openings detail, search API

##########################################################################################################

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Recipe-Suggestion

Backend

	Python Framwork Django, and Python

Front End
	Bootstrap, HTML,CSS, JQuerry, 
	
OS 
	Ubuntu
Database
	Django Defualt (While Developing sqlite3 was default selected, You can Choose any DB)

Run recipe-suggestion:

1) Create Virtual environment and activate it
	virtualenv {{environment name}}
	source bin/activate

2) Install requirements
	pip install -r requirement.txt

3) CD(Change Directory/Folder) TO magical_project where manage.py file exist
	
	python manage.py makemigrations
	python manage.py migrate

4) Run the app 
	python manage.py runserver 0.0.0.0:8000

5) Access the app at URL http://127.0.0.1:8000/ Using Browser

6) Log in Admin (Where You can add Information)
	http://127.0.0.1:8000/admin

	username : root
	password : superuser

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

