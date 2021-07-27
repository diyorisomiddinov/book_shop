from django.db import models


class BookHistoryModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class AuthorModel(models.Model):
    name = models.CharField(max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class BookModel(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT, related_name='books')
    about = models.TextField()
    booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
