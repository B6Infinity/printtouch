from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', view=views.home, name='home'),
    path('dashboard', view=views.home, name='dashboard'),
    path('accounts', view=views.accounts, name='accounts'),
    path('hoardings', view=views.hoardings, name='hoardings'),
    path('customers', view=views.customers, name='customers'),
    
    path('login', view=views.loginpage, name='login'),
    path('handle_login', view=views.handle_login, name='handle_login'),
    path('logout', view=views.logoutuser, name='logout'),

]