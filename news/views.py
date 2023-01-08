from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


# class PostLeaning:
#    def __init__(self, post):
#        self.post = post
#        self.leaning = self.determine_leaning()
#    
#    def determine_leaning(self):
#        # Check the value of the "admin_leaning" field in the post model
#        if self.post.political_view == "Left":
#            return "Left"
#        elif self.post.political_view == "Right":
#            return "Right"
#        else:
#            return "Neutral"
