from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50, null = True)
    country = models.CharField(max_length=100, null = True)

    def __str__(self) -> str:
        return f"{self.name} from {self.country}"

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    code = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        verbose_name_plural = "Blog Categories"
        verbose_name = "Blog Category"

    def __str__(self) -> str:
        return f"{self.name} - {self.code}"

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=False, blank=False, editable=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    category = models.ManyToManyField(Category, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

