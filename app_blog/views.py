from django.shortcuts import render
# Create your views here.


def index(request):

    return render(request,'html_pages/index.html')

def about(request):

    return render(request,'html_pages/about.html')

def category(request):

    return render(request,'html_pages/category.html')

def contact(request):

    return render(request,'html_pages/contact.html')

def s_result(request):

    return render(request,'html_pages/search-result.html')

def post(request):

    return render(request,'html_pages/single-post.html')