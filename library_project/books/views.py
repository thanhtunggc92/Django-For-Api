from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Book


def BookListView(request):
    model=Book.objects.all()
    context={'model':model}
    return render(request,'book_list.html',context)


