from django.shortcuts import render

posts = [
    {'author': 'CoreyMS', 'title': 'Blog Post 1', 'content': 'First post content', 'date_posted': 'April 20, 2018'},
    {'author': 'Jane Doe', 'title': 'Blog Post 2', 'content': 'Second post content', 'date_posted': 'April 21, 2018'},
    {'author': 'John Doe', 'title': 'Blog Post 3', 'content': 'Third post content', 'date_posted': 'April 22, 2018'},
    {'author': 'Jane Doe', 'title': 'Blog Post 4', 'content': 'Fourth post content', 'date_posted': 'April 23, 2018'},
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request , 'blog/home.html' , context)
def about(request):
    return render(  request , 'blog/about.html' , {'title' : "ABOUT"})
