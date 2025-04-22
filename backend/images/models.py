from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image {self.id} - {self.description[:50]}"

    class Meta:
        ordering = ['-created_at'] 