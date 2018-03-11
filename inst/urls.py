from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from inst.views import login_redirect

urlpatterns=[
    # url(r'^$', views.login_redirect, name='login_redirect'),
    url('^$',views.index, name='index'),
    url(r'^$',views.profile,name = 'profile'),
    url(r'^$',views.timeline,name = 'timeline'),
    url(r'^pic/(\d+)', views.single_pic, name='single_pic'),
    url(r'^comment/(?P<id>\d+)', views.comment, name='comment'),
    # url(r'^user/(\d+)', views.user_details, name='userDetails'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^single_pic/(\d+)', views.single_pic, name='single_pic'),
    url(r'^send/', views.send, name='send'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/profile', views.upload_profile, name='upload_profile'),


]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

