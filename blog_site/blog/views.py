from django.shortcuts import render
from blog.models import Article


# Create your views here.
def blog_list(request):
    'select * from where show=true order by updated desc limit 5'
    articles = Article.objects.filter(show=True).order_by('-updated')[:5]
    return render(request, 'blog/blog-list.html', context={'articles': articles})

def blog_detail(request, id):
    instance = Article.objects.get(id=id)
    return render(request, 'blog/blog-detail.html', context={
        'article': instance
    })    