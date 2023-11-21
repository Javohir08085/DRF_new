from django.urls import path

from .views import BooksListAPIView,BookDetailAPIView,BookCreateAPIView,BookUpdateAPIView,BookDeleteAPIView


urlpatterns = [
    path('list/<int:pk>', BookDetailAPIView.as_view()),
    path('list', BooksListAPIView.as_view()),
    path('new', BookCreateAPIView.as_view()),
    path('update/<int:pk>', BookUpdateAPIView.as_view()),
    path('delete/<int:pk>', BookDeleteAPIView.as_view()),
]