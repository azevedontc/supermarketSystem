from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import Register

urlpatterns = [
    path('', views.index, name="index"),
    path('frios', views.frios, name="frios"),
    path('entrega', views.entrega, name="delivery"),
    path('volumes', views.volumes, name="volumes"),
    path('presente', views.presente, name="gift"),
    path('promocoes', views.promotions, name="promocoes"),
    path('funcionario', views.call_staff, name="call_staff"),
    path('search', views.search, name="search"),
    path('login', views.login_view, name="login"),
    path('register', Register.as_view(), name="register"),
    path('delete/account', views.delete_account, name="delete_account"),
    path('logout', views.logout_view, name="logout"),
]