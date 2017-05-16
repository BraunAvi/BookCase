from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    url(r'^review/(?P<review_id>\d+)/$', views.review_detail, name='review_detail'),
    url(r'^book/(?P<book_id>\d+)/$', views.book_detail, name='book_detail'),

    # ex: /review/5/
    # ex: /review/5/
    url(r'^review/new/$', views.review_new, name='review_new'),
    url(r'^book/new/$', views.book_new, name='book_new'),
    url(r'^review/(?P<pk>\d+)/edit/$', views.review_edit, name='review_edit'),
    # url(r'^book/(?P<pk>\d+)/edit/$', views.book_edit, name='book_edit'),

    # url(r'^book$', views.book_list, name='book_list'),
    # ex: /wine/5/
    # url(r'^book/(?P<book_id>[0-9]+)/$', views.book_detail, name='book_detail'),
]



"""
https://www.codementor.io/jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a

from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /wine/
    url(r'^wine$', views.wine_list, name='wine_list'),
    # ex: /wine/5/
    url(r'^wine/(?P<wine_id>[0-9]+)/$', views.wine_detail, name='wine_detail'),
]
"""
