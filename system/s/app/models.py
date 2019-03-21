from django.db import models

# Create your models here.


class Student(models.Model):
    User_id = models.AutoField(primary_key=True)

    UserName = models.CharField(max_length=24)
    PassWord = models.CharField(max_length=24)
    Email = models.CharField(max_length=30)
    LastChangeTime = models.DateTimeField(auto_now=True)

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
    Content = models.TextField()

    BMStartTime = models.DateTimeField()
    BMEndTime = models.DateTimeField()
    CTStartTime = models.DateTimeField()
    CTEndTime = models.DateTimeField()
    Kind=models.CharField(max_length=50)
    Level=models.CharField(max_length=50)
    Holder=models.CharField(max_length=300)
    Allower=models.CharField(max_length=300)
    Tag=models.TextField()
    ReleaseTime = models.DateTimeField(auto_now_add=True)

    LastChangeTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title
