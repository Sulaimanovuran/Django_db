from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    picture = models.ImageField(upload_to='news_images')
    created_date = models.DateField(auto_now_add=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_id': self.pk}) # /news/1/


    class Meta:
        ordering = ['title']


