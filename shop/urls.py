# urlpatterns = [
#     url(r'^$', views.shop, name='shop'),
#     url(r'^(?P<category_slug>[-\w]+)/$', views.shop, name='product_index_by_category'),
#     url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
#     url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
#     # url(r'^cart/$', views.cart_detail, name='cart_detail'),
#     # url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
#
# ]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shop, name='shop'),
    url(r'^cart/$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.shop, name='product_index_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
