from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    completed = models.BooleanField(default=False)
    created =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
