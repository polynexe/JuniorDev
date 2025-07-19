from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import ForeignKey

# Create your models here.

User = get_user_model()

class User(models.Model):
    portfolio_title = models.CharField(max_length = 100, blank = False)
    portfolio_description = models.TextField(max_length = 500, blank = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.portfolio_title

class Project(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    project_title = models.CharField(max_length = 100, blank = False)
    project_description = models.TextField(max_length = 500, blank = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Meta(models.Model):
    ordering = ['-created_at']

    def __str__(self):
        return f"{self.project_title} (by {self.user.portfolio_title})"