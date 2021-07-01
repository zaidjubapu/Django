# i have created this file - zaid
# code of video 5
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("<h1>hello iam zaid</h1>")

# def about(request):
#     return HttpResponse("hello iam zaid this is about function")

# def file(request):
#     files=open('one.txt',"r+")
#     return HttpResponse(files)

# code for video 7
# i have created this file - zaid
# def index(request):
#     return HttpResponse("Home")

# def removepunc(request):
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capfirst")

# def newlineremove(request):
#     return HttpResponse("newlineremove")
    
# def spaceremove(request):
#     return HttpResponse("spaceremove")

# def capfirst(request):
#     return HttpResponse("capfirst")

# def charcount(request):
#     return HttpResponse("charcount")

# code video 8

# def index(request):
#     # return HttpResponse("Home")
#     params={'name':'zaid','place':'bhatkal'}
#     return render(request, 'index.html',params)

# def removepunc(request):
#     return HttpResponse("remove punc")

# def newlineremove(request):
#     return HttpResponse("newlineremove")
    
# def spaceremove(request):
#     return HttpResponse("spaceremove <a href='/'>back</a>")

# def capfirst(request):
#     return HttpResponse("capfirst")

# def charcount(request):
#     return HttpResponse("charcount")


# code video 9

# 

# code video 10

def index(request):
    # return HttpResponse("Home")

    return render(request, 'index.html',)

def analyze(request):
    #get the text 
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    # print(removepunc)
    # print(djtext)
    if removepunc == "on":
        analyzed=""
        punctuationslist='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuationslist:
                analyzed=analyzed+char


        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse(djtext)
    #analyze the text
    # return HttpResponse(djtext)