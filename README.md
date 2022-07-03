# My Task Explanation
## 1. Make Simple Django App:
First of all we created a simple django app which shows us a heading of **Welcome to Linked Matrix**. In templates folder we created a *home.html* file which simply resulted in the app page.

## 2.Configuring Python Logging:
Secondly, I learnt how to configure python loging in django app. As it is required in a task to show time and IP address of the user in debug.log file. So in formatters I describe the format of our message i.e;{asctime} {message}.
```
import os

LOGGING ={
    'version':1,
    'loggers':{
        'django-request':{
            'handlers':['file'],
            'level':'INFO'
        }
    },
    'handlers':{
        'file':{
            'level':'INFO',
            'class':'logging.FileHandler',
            'filename':'./logs/debug.log',
            'formatter':'simple'
        }
    },
    'formatters':{
        'simple':{
            'format':'{asctime} {message}',
            'style':'{',
        }
    }
}
```
## 3.Configuring Redis with Django:
In second step I configured Redis with Django in *settings.py* file:
```
CACHE_TTL = 60

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "example"
    }
}
```
*TTL* is a time that an object is stored in a caching system before deletd or restored. As in our task it is 1 minutes so I set it to 60.
## 4.Making a Custom Middleware:
According to our task, it is required to get IP address and count them in custom middlewares. As middleware is a lightweight plugin that processes during request and response execution.Therefore when a user requests, getting and counting of IP address of the user will be implemented in custom middlewares.
The custom middleware'syntax is given as:
```
class FirstMiddleware:  
    def __init__(self, get_response):  
        self.get_response = get_response  
      
    def __call__(self, request):  
        response = self.get_response(request)  
        return response
```
## 5. Finding IP Address of the User:
The IP address is obtained from **request.META['REMOTE_ADDR']**.
I made a custom middleware named *getIpMiddleware.py* which stores the IP address of the user in debug.log file with the help og python logging which I configured in the second step.
```
import logging

class GetIpAddress(object):
    def __init__(self,get_response):
        self.get_response = get_response
             
    def __call__(self,request):
        response = self.get_response(request)
        logger = logging.getLogger("django-request")
        logger.info(request.META['REMOTE_ADDR'])
        return response
```
To activate this middleware, added it to middleware list in *settings.py* file.
## 6.Counting IP Address of the User:
I made one more custom middleware named *countIpMiddleware.py* in which I defined different groups of subscription of user with three categories:
**Gold,Silver and Bronze**.
Gold user will access the website 10 times per minute.
Silver user will access the website 5 times per minute.
Bronze user will access the website 2 times per minute.
**LOGIC:** For example when a gold user comes to the website the variable named **limit** will initialize to its maximum value i.e, 10 in this case.Then when the gold user will visit again the value will decrease to 9 and so on.So when gold user visits  10 times, he will have to wait for 1 minute until the cache will be restored.
```ip = request.META['REMOTE_ADDR']
        
        if ip in bronze:
            limit=2
        elif ip in silver:
            limit=5
        elif ip in gold:
            limit=10
        else:
            limit=1
            
        if ip not in cache:
            cache.set(ip,limit,timeout=60)
            return response
        elif cache.get(ip)>0:
            cache.set(ip,cache.get(ip)-1,timeout=60)
            return response
        elif cache.get(ip)==0:
            return HttpResponseForbidden("Please wait for 1 minute to access")
```
**From step 1 to step 6 the code is 100% working**
## 7. Dockerize Django App with Dockerfile:
First I installed docker engine and docker-desktop.
Then I write all the dependencies of my django app with this following command:
> pip freeze > requirements.txt
So in requirements.txt file all the dependencies of my django app will be written automatically.
Then I made **Dockerfile** in which I wrote instructions for **Docker Image**.
Docker Image is created with this following command:
> docker build --tag python-django .
> 
Docker image is a template for making **Docker Container**
Docker container is created with this command:
> docker run --publish 8000:8000 python-django
So docker image and docker container is made in docker-desktop but somehow docker container is not working. I configured the Docker correctlty but it is showing the error of Redis-port. 
**Thank you for reading and I hope I am able to comprehend my task.**
Regards:
Muhammad Usama
