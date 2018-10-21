from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from mysite.core import views as core_views


urlpatterns = [
    url(r'^$', core_views.god, name='god'),
    url(r'^home/$', core_views.home, name='home'),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    # url(r'^logout/$', core_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^home3/$', core_views.home3, name='home3'),
    url(r'^chennai/$', core_views.chennai, name='chennai'),
    url(r'^salem/$', core_views.salem, name='salem'),

]
