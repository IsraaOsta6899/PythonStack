from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('authors',views.index1),
    path('books/<int:BookID>',views.index2),
    path('authors/<int:AuthID>',views.index3),
    path('addBook', views.addBook),
    path('addAuthor', views.addAuthor),
    path('addauthtobook/<int:BookID>',views.addauthtobook),
    path('addbooktoauth/<int:authID>',views.addbooktoauth),
    
]