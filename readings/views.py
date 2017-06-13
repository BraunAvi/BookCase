# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Review, Book
from .forms import ReviewForm, BookForm
from django.shortcuts import redirect

from django.contrib.auth import logout
from django.http import HttpResponse

from django.template.defaulttags import register


def index(request):
    books = Book.objects.filter(adding_date__lte=timezone.now()).order_by('-adding_date')
    books=books[0:min(len(books),3)]
    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    reviews=reviews[0:min(len(reviews),3)]

    dict_review_rating_to_text(reviews)
    return render(request,
                  'readings/index.html',
                  {'reviews': reviews,
                   'books': books})

def dict_review_rating_to_text(reviews=[]):
    """ this function takes the list of reviews as input and return the text of the rating of these reviews"""
    text_rating={1: 'did\'nt like it so much',
                 2: 'thought it was OK',
                 3: 'Loved it!'}
    for i in range (0,len(reviews)):
        reviews[i].text_rating=text_rating[reviews[i].rating]
    return reviews

def review_list(request):
    # import pdb;
    # pdb.set_trace()
    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    dict_review_rating_to_text(reviews)
    return render(request,
                  'readings/review_list.html',
                  {'reviews': reviews})

def book_list(request):
    # import pdb;
    # pdb.set_trace()
    books = Book.objects.filter(adding_date__lte=timezone.now()).order_by('-adding_date')
    # dict_review_rating_to_text(books)
    return render(request,
                  'readings/book_list.html',
                  {'books': books})




def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    dict_review_rating_to_text([review]) # add a column with the rating text based on the dictionary above
    return render(request, 'readings/review_detail.html',
                  {'review': review})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = Review.objects.filter(book=book_id).order_by('-published_date')
    dict_review_rating_to_text(reviews)

    # reviews = Review(review.book=book.id, tagline='All the latest Beatles news.')
    return render(request, 'readings/book_detail.html',
                  {'book': book,
                   'reviews': reviews})

def review_new(request):
    if not request.user.is_authenticated():
        return redirect('readings:auth_error_message', error_type=1)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            review = form.save(commit=False)
            review.reviewed_by = request.user
            review.published_date = timezone.now()
            review.save()
            id=review.pk
            return redirect('readings:review_detail', review_id=id)
    else:
        form = ReviewForm()
    return render(request, 'readings/review_edit.html', {'form': form})


def book_new(request):
    if not request.user.is_authenticated():
        return redirect('readings:auth_error_message', error_type=1)
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            book = form.save(commit=False)
            book.added_by = request.user
            book.adding_date = timezone.now()
            book.save()
            # book = form.save()
            id = book.pk
            return redirect('readings:book_detail',book_id=id)
    else:
        form = BookForm()
    return render(request, 'readings/book_edit.html', {'form': form})

def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if review.reviewed_by!=request.user:
        return redirect('readings:auth_error_message', error_type=0)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.updated_date = timezone.now()
            review.save()
            return redirect('readings:review_detail', review_id=review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'readings/review_edit.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    # if review.reviewed_by!=request.user:
    #     return redirect('readings:auth_error_message', error_type=0)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.updated_date = timezone.now()
            book.save()
            return redirect('readings:book_detail', book_id=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'readings/book_edit.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('readings:review_list')

# def log_in(request):
#     logout(request)
#     return redirect('login')

def auth_error_message(request,error_type=0, message='',logged_in=''):
    error_type_get=request.get_full_path().rsplit('/',2)[-2] # get the last digit if the url (error-type)
    try: error_type_get =int(error_type_get)
    except: pass
    message = create_error_message(error_type=error_type_get)
    logged_in=request.user
    return render(request, 'readings/error_message.html',
                  {'message': message,
                   'logged_in':logged_in})


def create_error_message(error_type=0):
    if error_type == 0:
        message = "It looks as if you're trying to edit someone else's review. That's not nice ;)"
    elif error_type == 1:
        message = "You need to log-in before  registering your readings or books)"
    else: message = "Error No "+str(error_type)
    return message

