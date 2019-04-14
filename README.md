# Event_App
This repository contains the backend of Events App build using Django Rest Framework.

<br/>
Language and Framework used: Python; Django Rest Framework (DRF)
Database: SQLite
<br/>

**Setup Process:**
1.	Setup Virual environment for your OS platform or simply use docker. Activate the virtual environment. Or if using docker, simply run “docker-compose up”, then “docker exec -it web bash”
2.	Then run: “python pip install -r requirements.txt”
3.	cd eventapp
4.	python manage.py makemigrations
5.	python manage.py migrate
6.	python manage.py createsuperuser
7.	python manage.py runserver



**After setup,**
  1.	Open http://127.0.0.1:8000/admin in your browser and login with credentials created in the step 6 above. You’ll see the database admin once logged in.
In another tab:
  2.	APIs:
  	  <br>
	  http://127.0.0.1:8000/api/users/register/
	  <br>
	  http://127.0.0.1:8000/api/users/login/
	  <br>
    	  http://127.0.0.1:8000/api/users/setPreferences/
	  <br>
    	  http://127.0.0.1:8000/api/users/getEvents/
	  <br>
  3.	Once you register the user (ignore the warning/error as this error is handled inside virtual environment – ‘venv’ directory – which is not supported currently in DRF).
  4.	Go to the step 1 admin page and see the database, inside Users -> Profile, there will be the entry of the registered user. Login with the same user using login API.
  5.	Change the preferences with setPreferences, though it will not reflect inside the database as the permissions are required from the frontend to redirect the user if authenticated.
  6.	For getEvents API, one needs to enter the external API credentials to get the data – using Postman.



**Code:**
  1.	The eventapp is the root project folder. Users is the app (component in JS frameworks) folder.
  2.	The routing is handled through urls.py files inside eventapp and users app.
  3.	The API structure for all the APIs is written in views.py inside Users app. The data is serialized and deserialized using serializers.py all inside the users app.
  4.	For getEvents external API, the logic is written under the getEvents class in views.py and the call to the ecternal API is made using python ‘requests’ library.
  5.	The validation is carried out inside serializers.py for register and login APIs.
  6.	Inside models.py, profile class maintains data for preferences linked with primary key – user’s id – to normalize the database.
