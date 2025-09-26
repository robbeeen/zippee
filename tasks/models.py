import uuid
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Task(models.Model):
    slug = models.SlugField(unique=True, blank=True) # for better seo
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            unique_id = str(uuid.uuid4())[:8]
            self.slug = slugify(f"{self.title}-{unique_id}")
        super().save(*args, **kwargs)

