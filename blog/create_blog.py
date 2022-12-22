from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView
from .models import Post

class createBlogView(CreateView):
    template_name = "blog_crud/post_form.html"
    model = Post
    fields = "__all__"
    success_url = "/posts/create/done"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Write a New Blog"
        context["action"] = "create"
        return context

class updateBlogView(UpdateView):
    template_name = "blog_crud/post_form.html"
    model = Post
    fields = "__all__"
    success_url = "/posts/create/done"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title
        context["action"] = "update/"+self.object.slug
        return context

class SuccessAlertView(TemplateView):
    template_name = "blog_crud/created.html"