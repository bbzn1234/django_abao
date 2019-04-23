from django.urls import path
from django.conf.urls import *
from . import view, testdb
 
urlpatterns = [
    path('', view.hello),
    path('hello/', view.hello),
    url(r'^testdb$', testdb.testdb),
]
