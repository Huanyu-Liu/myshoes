from django.conf.urls import url
from . import views

app_name = 'product'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^(?P<product_id>[0-9]+)/show_case/$', views.show, name='show_case'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^buy/$',views.buy,name='buy'),
]