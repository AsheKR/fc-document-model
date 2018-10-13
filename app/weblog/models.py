from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField(lbank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_dele=models.CASCADE,
    )
    headline = models.CharField(max_length=255)
    pub_date = models.DateField(blank=True, null=True)
    authors = models.ManyToManyField(Author, blank=True)
    n_commoent = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.headline