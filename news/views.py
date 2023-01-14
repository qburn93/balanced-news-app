from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    if post.category == 'SPORTS':
        return render(request, 'blog/sports_post_detail.html', {'post': post})
    elif post.category == 'ECONOMY':
        return render(request, 'blog/economy_post_detail.html', {'post': post})
    elif post.category == 'POLITICAL':
        return render(request, 'blog/political_post_detail.html', {'post': post})
    else:
        return redirect('home')


def sports(request):
    return render(request, 'sports.html')


def economy(request):
    return render(request, 'economy.html')