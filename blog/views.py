from django.shortcuts import render
# Create your views here.


#some dummy post: 
posts = [{
    'author': 'Issa',
    'title': 'Blog Post 1', 
    'content': 'Blog Post Content', 
    'date_posted': '25 Jul, 2024'
    },
    {
    'author': 'Issa2',
        'title': 'Blog Post 2', 
        'content': 'Blog Post Content 2', 
        'date_posted': '25 Jul, 2024 (2)'
    }
]

#req->res return home page
def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':"about"})
