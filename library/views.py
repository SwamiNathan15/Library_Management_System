# from django.shortcuts import render
# def home(request):
#     return render(request, "home.html")
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Library Mangement System")

# from django.shortcuts import render
# from .models import Book

# def home(request):
#     books = Book.objects.all()

#     return render(request ,
#                   "home.html",
#                   {"books" : books}
#     )


# def book_detail(request , id):
#     book = Book.objects.get(id = id)
#     return render(request ,
#                   "book_detail.html" , 
#                   {"book" : book}
#     )




from django.shortcuts import get_object_or_404 , render , redirect
from .models import Book , BorrowRecord
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    books = Book.objects.all()

    return render(request ,
                  "home.html",
                  {"books" : books}
    )


def book_detail(request , id):
    book = get_object_or_404(Book , id = id)
    return render(request ,
                  "book_detail.html" , 
                  {"book" : book,
                   "user" : request.user
                   }
    )

@login_required


def borrow_book(request , id):
    print(request.user)
    print(request.user.groups.all())

    if not request.user.groups.filter(
        name = "Student"
    ).exists():
        return HttpResponse("Access Denied")
    
    book = get_object_or_404(Book , id = id)

    if BorrowRecord.objects.filter(
        user = request.user,
        book = book
    ).exists():
        return HttpResponse("You have already boorowed this book")
    
    if not book.is_available:
        return HttpResponse("This book is currently unavailable")
    
    BorrowRecord.objects.create(
        user = request.user ,
        book = book         
    )

    book.is_available = False
    book.save()

    return redirect("/")


def my_books(request):
    borrowed_books = BorrowRecord.objects.filter(
        user = request.user
    )
    return render(request,
        "my_books.html",
        {
            "borrowed_books" : borrowed_books
        }
    )


def add_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        price = request.POST["price"]
        Book.objects.create(
            title = title,
            author = author,
            price = price
        )
        return redirect('/')
    return render(request , "add_book.html")

def edit_book(request , id):
    return HttpResponse("Edit Book Page")

def check_role(request):
    if request.user.groups.filter(
        name = "Librarian"
    ).exists():
        return HttpResponse("You are a librarian")
    
    return("You are not a Librarian")

@login_required
def return_book(request , id):
    record = get_object_or_404(BorrowRecord , id = id)

    if record.user != request.user:
        return HttpResponse("Access Denied")
    
    record.book.is_available = True
    record.book.save()
    record.delete()

    return redirect("/my-books/")



