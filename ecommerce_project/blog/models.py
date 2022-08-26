from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
 
    def __str__(self):
        return self.title

class Meta:
    verbose_name = 'Article'
    verbose_name_plural = 'Articles'
