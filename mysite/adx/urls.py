from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.signIn),
	url(r'^post_signin/', views.post_signin, name='post_signin'),
    url(r'^signup/',views.signup, name='signup'),
	url(r'^postsignup/',views.postsignup, name='postsignup'),
    url(r'^create/',views.create, name='create'),
    url(r'^post_create/', views.post_create, name='post_create'),
    url(r'^about/', views.about, name='about'),
    url(r'^logout', views.log_out, name='logout'),

]