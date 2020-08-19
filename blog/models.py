from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="images/blogs/")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
