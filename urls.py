from django.conf.urls import url, include
from app import views as app_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'celery_test.views.home', name='home'),
    # uurl(r'^celery_test/', include('celery_test.foo.urls')),
	url(r'^celery_test/', app_views.test_celery),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]