from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    CreateAPIView, UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.views import APIView

from django.db.models import Max

from .models import Books
from .serializers import BooksSerializer, BookDetailsSerializer


# Create your views here.
class BooksListAPIView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    # def get_queryset(self):
        # if 'name' in self.request.GET and 'value' in self.request.GET:
    #         # match self.request.GET['name']:
    #         def switch(case):
    #             if case == 'author':
    #                 # key_word = self.request.GET['value']
    #                 print("Books.objects.filter(book_author__icontains=key_word)")
    #             elif case == 'title':
    #                 # key_word = self.request.GET['value']
    #                 print("Books.objects.filter(book_title__icontains=key_word)")
    #             elif case == 'desc':
    #                 # key_word = self.request.GET['value']
    #                 print("Books.objects.filter(book_desc__icontains=key_word)")
    #             else:
    #                 # key_word = self.request.GET['value']
    #                 print("Books.objects.filter(book_author__icontains=key_word) | Books.objects.filter(book_desc__icontains=key_word) | Books.objects.filter(book_author__icontains=key_word)")
    #     else:
    #         queryset = Books.objects.all()

        # if 'filter' in self.request.GET:
        # if 'to' in self.request.GET or 'from' in self.request.GET:
        #     if 'to' not in self.request.GET:
        #         start_price = self.request.GET['from']
        #         queryset = queryset.filter(book_price__gte=start_price)
        #     elif 'from' not in self.request.GET:
        #         final_price = self.request.GET['to']
        #         queryset = queryset.filter(book_price__lte=final_price)
        #     else:
        #         start_price = self.request.GET['from']
        #         final_price = self.request.GET['to']
        #         queryset = queryset.filter(book_price__range=(start_price, final_price))
        # # print(queryset)
        # return queryset


class BookDetailAPIView(RetrieveAPIView):
    serializer_class = BookDetailsSerializer
    queryset = Books.objects.all()


class BookCreateAPIView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookUpdateAPIView(UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookDeleteAPIView(DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer