from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='')
    tech_stack = models.CharField(max_length=1000)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message= models.TextField()

    def __str__(self):
        return self.name