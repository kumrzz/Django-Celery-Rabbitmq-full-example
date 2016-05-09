## Django, Celery and Rabbitmq example ##

Basic example that shows how to interact with django, celery and rabbitmq to process jobs.  
  
Example mostly based on [django-celery's](https://github.com/ask/django-celery/tree/master/examples) example.

Find the the blog post here: [http://simondlr.com/post/24479818721/basic-django-celery-and-rabbitmq-example](http://simondlr.com/post/24479818721/basic-django-celery-and-rabbitmq-example).

Kumar's log(fukin about with the code and adapting to my win env):  
https://www.rabbitmq.com/management.html  
C:\Program Files\RabbitMQ Server\rabbitmq_server-3.6.1\sbin\rabbitmq-plugins enable rabbitmq_management  
that allowed me to monitor shiz on a browser @ http://localhost:15672/  
user/pw = guest (default)  
git clone https://github.com/kumrzz/Django-Celery-Rabbitmq-full-example.git  
pip install django-celery  
cd Django-Celery-Rabbitmq-full-example  
python manage.py makemigrations  
python manage.py migrate --fake-initial (coz simple migrate didn't work)  
kicked off rabbitmq from windows: RabbitMQ Service - start  
python manage.py celeryd --loglevel=info  
http://127.0.0.1:8000/celery_test/  
checked rabbitmq on http://localhost:15672/  for action  
I found results were similar without running celeryd, just had fewer amqp instances acc to rabbitmqmgr  
