# from django.urls import path
# from . import views

# urlpatterns = [
#     path('' , views.home)
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home),
    path('books/<int:id>/' , views.book_detail),
    path('add-book/' , views.add_book),
    path('edit-book/<int:id>/' , views.edit_book),
    path('check-role/' , views.check_role),
    path('borrow/<int:id>/' , views.borrow_book , name = 'borrow_book'),
    path('my-books/' , views.my_books , name = 'my_books'),
    path('return-book/<int:id>/' , views.return_book , name = 'return_book'),
]