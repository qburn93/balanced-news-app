from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class NewsPostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'news_detail.html',
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    if post.category == 'SPORTS':
        return render(request, 'blog/sports_post_detail.html', {'post': post})
    elif post.category == 'ECONOMY':
        return render(request, 'economy_post_detail.html', {'post': post})
    elif post.category == 'POLITICAL':
        return render(request, 'post_detail.html', {'post': post})
    else:
        return render(request, 'blog/default_post_detail.html', {'post': post})


def sports(request):
    return render(request, 'sports.html')


def economy(request):
    return render(request, 'economy_post_detail.html')