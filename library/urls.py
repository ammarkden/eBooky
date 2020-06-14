from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
path('', views.index, name= 'home'),
path('books', views.get_books, name = 'books'),
path('login', views.log_in, name= 'login'),
path('logout', views.log_out, name= 'logout'),
path('profile/<int:ID>', views.show_profile, name= 'profile'),
path('book/<str:bookName>', views.get_book, name = 'book_details'),
path('category/<int:catID>', views.get_category, name = 'category'),
path('search/<str:bookName>', views.get_search, name = 'search'),
path('addtolist/<int:bookID>', views.add_to_list, name = 'addtolist'),
path('changeicon/<int:ID>/', views.change_photo, name = 'changeicon')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
