from django.db import models

# Create your models here.

class blogPosts(models.Model):
    postTitle = models.CharField(max_length=70)
    postAuthor = models.CharField(max_length=40)
    postDate = models.DateField(auto_now_add=True)
    postSummary = models.TextField()
    postContent = models.TextField()
    #postImages = 
