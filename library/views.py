from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from .models import *
from library.forms import newForm
from django.shortcuts import redirect
def index(req):
    context ={
        'Category' : Category.objects.order_by('categoryName'),
        'Books' : Book.objects.order_by('bookName'),
                }
    return render(req, 'library/home.html', context)

def get_book(req, bookName):
    context = {
        'Category': Category.objects.order_by('categoryName'),
         'books' :  Book.objects.get(bookName = bookName),
          }  
    return render(req, 'library/details.html', context)

def log_in(req):
    if req.user.is_authenticated:
        return redirect('/')
    else:
        if req.method == 'POST':
            if req.POST.get('submit_register'):
                form = newForm(req.POST)
                context = {'form': form}
                if form.is_valid():
                    form.save()
                    return render(req, 'library/login.html',)
                else:
                    context = {'form': form, 'Error': 'Invalid Data'}
                    return render(req, 'library/login.html',context)
            elif req.POST.get('submit_login'):
                username = req.POST['username']
                userpassword = req.POST['userpassword']
                user = authenticate(req, username = username, password = userpassword)
                if user is not None:
                    form = newForm(req.POST)
                    login(req,user)
                    context ={'Category': Category.objects.all(),
                    'Books': Book.objects.all()}
                    return redirect('/')
                else:
                    form = newForm(req.POST)
                    context = {'message': 'Invalid Username / Password', 
                    'form': form}
                    return render(req, 'library/login.html', context)
        else:
            form = newForm(req.POST)
            context = {'form': form, 'newForm' : newForm}
            return render(req, 'library/login.html', context)

def get_category(req, catID):
    categoryName = Category.objects.get(id = catID )
    context = {
        'Category': Category.objects.get(id = catID ),
        'all_Category': Category.objects.order_by('categoryName'),
    }
    return render(req, 'library/category.html', context)

def get_search(req, bookName):
    context = {
        'books': Book.objects.get(bookName = bookName),
    }
    return render(req, 'library/search.html', context)

def show_profile(req, ID):
    context = {
        'Profile': Profile.objects.get(id= ID), 
    }
    return render(req, 'library/profile.html', context)
    
def get_books(req):
    context = {'Books' : Book.objects.order_by('bookName')}
    return render(req, 'library/books.html', context)

def add_to_list(req, bookID):
    if req.user.is_authenticated:
        user = Profile.objects.get(id = userID)
        books = Book.objects.get(id = bookID) 
        mylist = books.booklist = books
        context = {
            'books': mylist
        }
        return render(req, 'library/profile.html', context)
    else:
        context = {'warning': 'you have to be logged in'}
        return redirect('/login')

def log_out(req):
    context ={
        'Category' : Category.objects.all(),
        'Books' : Book.objects.all(),}
    logout(req)
    return render(req, 'library/home.html', context)

def change_photo(req, ID):
    imgURL = req.POST['imgURL']
    user = Profile.objects.get(id = ID)
    user.profileIcon = str(imgURL)
    user.save()
    return redirect("/profile/" + str(ID))





    


