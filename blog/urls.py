from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.post_list,name='post_list'),
	url(r'^hi/$',views.post_list2,name='post_list2'),
]