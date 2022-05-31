"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from todo.views import todoView, addTodo, deleteTodo, coverImage
from todo import views

urlpatterns = [
    path('', views.CoolerBook, name='CoolerBook'),
    path('CoolerBook.html', views.CoolerBook, name='CoolerBook'),
    path('CoolerBookAboutUs.html',
         views.CoolerBookAboutUs,
         name='CoolerBookAboutUs'),
    path('CoolerBookArticle.html',
         views.CoolerBookArticle,
         name='CoolerBookArticle'),
    path('CoolerBookContacts.html',
         views.CoolerBookContacts,
         name='CoolerBookContacts'),
    path('CoolerBookRegister.html',
         views.CoolerBookRegister,
         name='CoolerBookRegister'),
    path('CoolerBookSuccess.html',
         views.CoolerBookSuccess,
         name='CoolerBookSuccess'),
    path('admin/', admin.site.urls),
    # path('', todoView),
    # path('addTodo/', addTodo),
    # path('deleteTodo/<int:todo_id>/', deleteTodo),
    # path('app.png', coverImage),
 
]
