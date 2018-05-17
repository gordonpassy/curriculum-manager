from django.db import models

# Create your models here.

class Chapter(models.Model):
    number = models.IntegerField(max_length=30)

    def __str__(self):
        return self.name

    def save_chapter(self):
        self.save()

    def delete_chapter(self):
        self.delete()

class Page(models.Model):
    number = models.IntegerField(max_length=30)

    def __str__(self):
        return self.name

    def save_page(self):
        self.save()

    def delete_page(self):
        self.delete()

class Subject(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    chapter = models.ForeignKey(Chapter)
    page = models.ForeignKey(Page)
    time_uloaded = models.DateTimeField(auto_now_add=True, null=True)