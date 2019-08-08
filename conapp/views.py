from django.shortcuts import render
from .booinfo import Book
from .services import *

def index(request):
    return render(request, 'index.html')

def submit(request):
    # bid = request.POST['bid']
    bnm = request.POST['bnm']
    bpub = request.POST['bpub']
    bath = request.POST['bath']
    bprice = request.POST['bprice']
    bqty = request.POST['bqty']
    # print('this is our data',bid,bnm,bpub,bath,bprice,bqty)
    bob = Book(bnm=bnm,bpub=bpub,bath=bath,bprice=bprice,bqty=bqty)
    BookImpl.add_book(bob)
    return render(request,'index.html')
