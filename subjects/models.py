from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chapter(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return self.name

    def save_chapter(self):
        self.save()

    def delete_chapter(self):
        self.delete()

class Page(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return self.name

    def save_page(self):
        self.save()

    def delete_page(self):
        self.delete()

class Users(models.Model):
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user.username

    def save_users(self):
        self.save()

    def delete_users(self):
        self.delete()

class Subject(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    chapter = models.ForeignKey(Chapter)
    page = models.ForeignKey(Page)
    time_uloaded = models.DateTimeField(auto_now_add=True, null=True)

    def save_subject(self):
        self.save()

    def delete_subject(self):
        self.delete()
