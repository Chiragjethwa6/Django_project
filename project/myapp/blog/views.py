from django.shortcuts import render
from .models import post

# posts = [
#     {
#         'author' : 'chirag',
#         'title' : 'hello world',
#         'content' : 'first pro',
#         'date_posted' : 'aug 12'
#     },
#     {
#         'author' : 'chira',
#         'title' : 'hello world 2',
#         'content' : 'second pro',
#         'date_posted' : 'aug 13'
#     }
# ]

# Create your views here.
def home(request):
    context = {
        'posts' : post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})    
