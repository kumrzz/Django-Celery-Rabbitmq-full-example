# Create your views here.
from django.http import HttpResponse
from app import tasks

def test_celery(request):
	result = tasks.sleeptask.delay(10)
	result_one = tasks.sleeptask.delay(15)
	result_two = tasks.sleeptask.delay(20)
	return HttpResponse(result.task_id + ' -- ' + result_one.task_id + ' -- ' + result_two.task_id)