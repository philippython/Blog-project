from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
