from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.IntegerField()
    is_available = models.BooleanField(
        default = True
    )

    def __str__(self):
        return self.title
    

class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name = "borrowed_books") 

    book = models.ForeignKey(Book, on_delete=models.CASCADE , related_name = "borrowed_records")  

    borrowed_at = models.DateTimeField(
        auto_now_add=True
    )
    returned = models.BooleanField(
        default = False
    )

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"