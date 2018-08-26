from django.db import models

# Create your models here.


class Student(models.Model):
    User_id = models.AutoField(primary_key=True)

    UserName = models.CharField(max_length=20)
    Uid_LastChangeTime = models.DateTimeField(auto_now_add=True)

    PassWord = models.CharField(max_length=20)
    Pwd_LastChangeTime = models.DateTimeField(auto_now_add=True)

    Email = models.CharField(max_length=30)

    Tag = models.TextField(max_length=30, null=True)

    def __str__(self):
        return self.UserName


class ClubAdmin(Student):
    Club = models.charField(max_length=30)

    def __str__(self):
        return self.UserName


class Activity(models.Model):
    Act_id = models.AutoField(primary_key=True)

    Title = models.CharField(max_length=100)
    Title_LastChangeTime = models.DateTimeField(auto_now_add=True)
    
    Content = models.charField(max_length=400)
    Content_LastChangeTime = models.DateTimeField(auto_now_add=True)

    StartTime = models.DateTimeField()
    St_LastChangeTime = models.DateTimeField(auto_now_add=True)

    EndTime = models.DateTimeField()
    Et_LastChangeTime = models.DateTimeField(auto_now_add=True)

    ReleaseTime = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.Title
