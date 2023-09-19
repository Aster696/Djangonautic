from django.shortcuts import render

def article_list(request): 
    return render(request, 'articles/articles_list.html')