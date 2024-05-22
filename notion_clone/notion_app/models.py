from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255, default='project')
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"Проект '{self.name}'"

class Doc(models.Model):
    name = models.CharField(max_length=255, default='doc')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='docs')
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return f"Документ '{self.name}'"
