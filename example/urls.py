from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_func', views.data_list_func_test, name='test_func'),

]
