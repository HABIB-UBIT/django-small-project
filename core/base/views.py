from django.shortcuts import render
from .models import * 
from .forms import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

# def index(request):
#     return render(request, 'base/index.html')

def tweet_list(request):
    tweets= Tweet.objects.all()
    context= {'tweets': tweets}

    return render(request, 'base/tweet_list.html', context)

def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet= form.save(commit= False)
            tweet.user= request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form= TweetForm()
        context= {'form':form}
    return render(request, 'base/tweet_form.html', context)

def tweet_update(request,pk):
    # tweet= get_object_or_404(Tweet,id=pk, user= request.user)
    tweet= Tweet.objects.get(id=pk)
    form= TweetForm(instance=tweet)
    if request.user != tweet.user:
        return HttpResponse("You are not allowed to edit this tweet")
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance= tweet )
        if form.is_valid():
            tweet= form.save(commit= False)
            tweet.user= request.user
            tweet.save()
            return redirect('tweet_list')
    else: 
        form= TweetForm(instance=tweet)
        context= {'form':form}
    return render(request, 'base/tweet_form.html', context)


def tweet_delete(request,pk):
    # tweet= get_object_or_404(Tweet, id=pk, user= request.user)
    tweet= Tweet.objects.get(id=pk)
    if request.user != tweet.user:
        return HttpResponse("You are not allowed to edit this tweet")
    if request.method =="POST":
        tweet.delete()
        return redirect('tweet_list')
    context= {'tweet':tweet}
    return render(request, 'base/tweet_delete.html', context)

