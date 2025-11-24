from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    technologies = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # e.g., "Frontend", "Backend"
    proficiency = models.IntegerField(default=50)  # 0-100
    
    def __str__(self):
        return self.name