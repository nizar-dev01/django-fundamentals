from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic.base import TemplateView
from django.views.generic import ListView
# Create your views here.

class StartingPageView(TemplateView):
    template_name = "blog/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by("-date")[:3]
        return context
    

class PostListView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"
    
class SinglePostView(TemplateView):
    template_name = "blog/post-detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, slug = kwargs["slug"])
        context["post"] = post
        context["tags"] = post.tags.all()
        return context

