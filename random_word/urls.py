from django.urls import path, include
from . import views

urlpatterns = [
    # path('', include('Survey_app1.urls')),
    path('', views.index),
    path('process_randword', views.process_randword),
    # path('count_att', views.count_att)
]
