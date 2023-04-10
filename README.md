# Polling Service
This service queries resources at the specified url in the configuration file (for this project, separate applications with views were created that can be accessed). Data from resources comes to the service in various formats, after which they are parsed and saved to the database. If the condition is met (the sum of real numbers in the database for the current day is more than 1000), a post-request is made to a third-party service (which is also implemented as a separate application within the framework of this project).
### Main functionality:
* **Poll three services to get data**
* **If the condition is met - a post-request for a third-party service**
* **Separate views for displaying data from the database, as well as events (fixing post-requests to a third-party service)**

### Requirements
* Language: **Python 3.11**
* Frameworks: **Django 4.2** and **Django Rest Framework 3.14.0** and **Celery 5.2.7**
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
