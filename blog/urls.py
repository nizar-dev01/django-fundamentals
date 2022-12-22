from django.urls import path
from . import views
from . import create_blog

urlpatterns = [
    path("", views.StartingPageView.as_view(), name = "starting-page"),
    path("posts/", views.PostListView.as_view(), name = "posts-page"),
    path("posts/create", create_blog.createBlogView.as_view()),
    path("posts/create/done", create_blog.SuccessAlertView.as_view()),
    path("posts/update/<slug:slug>", create_blog.updateBlogView.as_view()),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name = "post-detail-page"),
]
