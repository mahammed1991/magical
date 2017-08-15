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
	Django Defualt (While Developing sqlite3 was default selected, You can Choose any DB / 
	Dont change DB as of now Keep sqlite3 as it is to check working flow of the app)

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

	username : root  ,
	password : superuser

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Project Description 

A simple django application for storing the details of the companies and employees

After succefully running the app, we have different Tabs such as  Home, Company, Employee Details, and Job Openings
We can find searching area within the home tab here search result is shown based on search keys, remaing tabs are can be used to see all listed data of as there tab name indicates.

We have three filter option on home tab seacrhing 1) Search Job Openigs 2)Search Employees On Role 3)Search Company
incase if you dont select any checkbox, searching result will come from all three tables, if you check any check box then searching result will be from checked respective table. 

we also have a admin link at right top corner which directs to log in django admin panal where we can upload the information/data
username : root and password is superuser

 
 



