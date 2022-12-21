from django.shortcuts import render
from datetime import date
from django.http import Http404
# Create your views here.
post_list = [
    {
        "slug": "going-to-the-woods",
        "image": "woods.jpg",
        "author": "Carl Simson",
        "date": date(2020, 12, 10),
        "title": "Into The Woods",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't prepared for what happened whilst I was enjoying the veiw!",
        "contents": [
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto. Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
        ]
    },
    {
        "slug": "all-about-coding",
        "image": "coding.jpg",
        "author": "Max",
        "date": date(2022, 6, 20),
        "title": "All About Coding",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't prepared for what happened whilst I was enjoying the veiw!",
        "contents": [
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto. Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
        ]
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "John Carter",
        "date": date(2022, 5, 20),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't prepared for what happened whilst I was enjoying the veiw!",
        "contents": [
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto. Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
        ]
    },
    {
        "slug": "art-of-painting",
        "image": "painting.jpeg",
        "author": "Leo Tenston",
        "date": date(2022, 5, 20),
        "title": "The Art of Oil Painting",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't prepared for what happened whilst I was enjoying the veiw!",
        "contents": [
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto. Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nisi vero inventore tempore eaque distinctio facere nemo natus, odit, placeat voluptatibus maiores veritatis vel, ipsa velit assumenda laborum amet perferendis architecto.",
        ]
    },
]


def get_data(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(post_list, key=get_data)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": post_list
    })


def single_post(request, slug):
    post = [post for post in post_list if post['slug'] == slug]
    if(len(post)>0):
        return render(request, "blog/post-detail.html", {
            "post": post[0]
        })
    else:
        raise Http404()

