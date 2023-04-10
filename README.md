# Polling Service
This service queries resources at the specified urls in the configuration file (for this project, separate applications with views were created that can be accessed). Data from resources comes to the service in various formats, after which they are parsed and saved to the database PostgreSQL. If the condition is met (the sum of float numbers in the database for the current day is more than 1000), a post-request is made to a third-party service (which is also implemented as a separate application within the framework of this project).

### Main functionality:
* **Poll three services to get data**
* **If the condition is met - a post-request for a third-party service**
* **Separate views for displaying data from the database, as well as events (fixing post-requests to a third-party service)**

### Requirements:
* Language: **Python 3.11**
* Frameworks: **Django 4.2**, **Django Rest Framework 3.14.0** and **Celery 5.2.7**
* Databases: **PostgreSQL 15** and **Redis**

## Preparing
Create **.env** file in the main **backend** directory and fill it in as in the example .env.example:

        # Django conf
        SECRET_KEY='secret'
        
        # DB PostgreSQL conf
        DB_USERNAME=postgres
        DB_PASSWORD=postgres
        DB_NAME=postgres
        DB_HOST=postgres
        DB_PORT=5432
        
        # Redis conf
        REDIS_HOST=redis
        REDIS_PORT=6379
        REDIS_DB=0
        
        # URLs services
        RESOURCE_FIRST_URL='http://127.0.0.1:8000/resource-first/resource/'
        RESOURCE_SECOND_URL='http://127.0.0.1:8000/resource-second/resource/'
        RESOURCE_THIRD_URL='http://127.0.0.1:8000/resource-third/resource/'
        POST_SERVICE_URL='http://127.0.0.1:8000/post-service/events/'
        
        # Main app url
        MAIN_APP_URL='http://127.0.0.1:8000/main-service/get-data/'

## Application launch
Run the following command in a terminal from the root directory of the project:

    docker-compose up

Then go into the application container by running the following command in an additional terminal window:
    
    docker exec -it backend sh

Create a superuser in the same terminal window:
    
    python manage.py createsuperuser

### All done!

## Project structure:
* **main_app** - the main service that polls resources, and if the condition is met (the sum of real numbers is greater than 1000 for the current day in the PostgreSQL database in the Data model), it makes a post-request by url to the receiving_service. 
        See all responses from requests: **'http://127.0.0.1:8000/main-service/get-data/'**

* **receiving_service** - a service that receives the time of the event by post-request  and writes it to the database in the Event model (if the condition of the sum of numbers is greater than 1000 for the current day in the PostgreSQL database in the Data model). 
        View all events: **'http://127.0.0.1:8000/post-service/events/'**

* **resource_first** - a service that sends data in xml format on a get-request like: `<root><date>12-02-2023 00:00</date><data>NUMBER</data></root>`. 
        Get response from service: **'http://127.0.0.1:8000/resource-first/resource/'**

* **resource_second** - a service that sends data in json format on a get request like this: `{ "data": "NUMBER", "date":"2023-02-12 00:00"}`. 
        Get response from service: **'http://127.0.0.1:8000/resource-second/resource/'**

* **resource_third** - a service that sends data in the string format on a get request: `"1676160000 NUMBER"`. 
        Get response from service: **'http://127.0.0.1:8000/resource-third/resource/'**
