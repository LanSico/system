from django.db import models

# Create your models here.


class Student(models.Model):
    User_id = models.AutoField(primary_key=True)

    UserName = models.CharField(max_length=20)
    PassWord = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    LastChangeTime = models.DateTimeField(auto_now_add=True)

    Tag = models.TextField(max_length=30, null=True)

    def __str__(self):
        return self.UserName


class ClubAdmin(Student):
    Club = models.CharField(max_length=30)

    def __str__(self):
        return self.UserName


class Activity(models.Model):
    Act_id = models.AutoField(primary_key=True)

    Title = models.CharField(max_length=100)
    Content = models.CharField(max_length=400)

    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    ReleaseTime = models.DateTimeField(auto_created=True)

    LastChangeTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
