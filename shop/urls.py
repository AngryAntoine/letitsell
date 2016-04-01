from django.conf.urls import url, include
from . import views

urlpatterns = [

	url(r'^$', views.shop, name='shop'),
	url(r'^(?P<id>\d+)/$', views.product_detail, name='product_detail'),

]
