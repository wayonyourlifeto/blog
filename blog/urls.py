from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView #new

urlpatterns = [
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'), #new 26/06
    path('post/new/', BlogCreateView.as_view(), name='post_new'), #new 26/06
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail') #new 24/06

]