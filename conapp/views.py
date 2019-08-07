from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def submit(request):
    bid = request.POST['bid']
    bnm = request.POST['bnm']
    bpub = request.POST['bid']
    bath = request.POST['bath']
    bprice = request.POST['bprice']
    bqty = request.POST['bqty']
    print('this is our data',bid,bnm,bpub,bath,bprice,bqty)
    return redirect, HttpResponse('submitted')