"""
URL configuration for workFlow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('intro/', views.intro, name='intro'),
    path('home/', views.home, name='home'),
    path('candidati/<int:offerta_id>/', views.candidati, name='candidati'),
    path('candidati_2/<int:offerta_id>/', views.candidati_2, name='candidati_2'),
    path('chat/<int:cand_id>/', views.chat, name='chat'),
    path('favourite/<int:offerta_id>/', views.favourite, name='favourite'),
    path('favourite_2/<int:offerta_id>/', views.favourite_2, name='favourite_2'),
    path('cancella_offerta/<int:offerta_id>/', views.cancella_offerta, name='cancella_offerta'),
    path('get_new_messages/<int:cand_id>/<int:last_message_id>/', views.get_new_messages, name='get_new_messages'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('addOfferta/', views.addOfferta, name='addOfferta'),
    path('logout/', views.logout, name='logout'),
    path('candidature/', views.candidature, name='candidature'),
    path('preferiti/', views.preferiti, name='preferiti'),
    path('accetta_candidatura/<int:cand_id>/', views.accetta_candidatura, name='accetta_candidatura'),
    path('cancella_candidatura/<int:cand_id>/', views.cancella_candidatura, name='cancella_candidatura'),
    path('admin/', admin.site.urls, name='admin'),
]