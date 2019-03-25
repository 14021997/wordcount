from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter
def homepage(request):
    return render(request,'home.html')

def count(request):
    data=request.GET['fulltextarea']
    data1=list(data.split())
    lenW=len(data1)
    worddict={}
    for word in data1:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word]=1
    sortedlist=sorted(worddict.items(),key=itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':data,'words':lenW ,'worddicts':sortedlist})

def about(request):
    return render(request,'about.html')