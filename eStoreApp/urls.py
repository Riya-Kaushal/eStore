from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
	# url(r'^homepage/', views.homepage, name='homepage'),
	url(r'^homepage/mobile', views.homepage_mobile, name='homepage_mobile'),
	url(r'^homepage/laptop', views.homepage_laptop, name='homepage_laptop'),
    url(r'^add-product/', views.add_product, name='add_product'),
    url(r'^update-product/', views.update_product, name='update_product'),
    url(r'^delete-product/', views.delete_product, name='delete_product'),
    url(r'^login/$', views.login_view, name='login'),
   	url(r'^logout/$', views.logout_view, name='logout'),
   	url(r'^register/$', views.register, name='register')
]