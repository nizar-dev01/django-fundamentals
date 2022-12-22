from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.CharField(max_length=120, null=False, blank=False)
    image = models.ImageField(upload_to="images")
    date = models.DateField(auto_now=True)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, related_name="posts")