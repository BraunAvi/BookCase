# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Review, Book
from .forms import ReviewForm, BookForm
from django.shortcuts import redirect
from django.template.defaulttags import register



def review_list(request):
    # import pdb;
    # pdb.set_trace()

    reviews = Review.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    reviews.text_rating=[]
    text_rating={1: 'did\'nt like it so much',
                 2: 'thought it was OK',
                 3: 'Loved it!'}
    for i in range (0,len(reviews)):
        reviews[i].text_rating=text_rating[reviews[i].rating]
        print reviews[i].reviewed_by.username,reviews[i].text_rating

    return render(request,
                  'readings/review_list.html',
                  {'reviews': reviews})

def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'readings/review_detail.html', {'review': review,
                                                           'reviews': 1,})
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'readings/book_detail.html', {'book': book})

def review_new(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            review = form.save(commit=False)
            # review.reviewed_by = request.user
            review.published_date = timezone.now()
            review.save()
            id=review.pk
            return redirect('readings:review_detail', review_id=id)
    else:
        form = ReviewForm()
    return render(request, 'readings/review_edit.html', {'form': form})


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('readings:book_detail',book_id=book.pk)
    else:
        form = BookForm()
    return render(request, 'readings/book_edit.html', {'form': form})

def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.published_date = timezone.now()
            review.save()
            return redirect('readings:review_detail', review_id=review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'readings/review_edit.html', {'form': form})

