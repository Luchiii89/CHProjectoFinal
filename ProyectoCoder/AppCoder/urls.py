from django.urls import path
from AppCoder import views


urlpatterns = [
   
    path('', views.start, name="Start"),
    path('books', views.newBook, name="Books"),
    path('authors', views.newAuthor, name="Authors"),
    path('editorials', views.editorials, name="Editorials"),
    path('bookshops', views.bookshops, name="Bookshops"),
    # path('getBookByGenre/', views.getBookByGenre),
]