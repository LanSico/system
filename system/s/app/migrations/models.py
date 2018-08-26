from django.db import models

# Create your models here.


class Student(models.Model):
<<<<<<< HEAD
    User_id = models.AutoField(primary_key=True)
=======
    Id=models.Autofield()
>>>>>>> cb70de47530da7931edd3f250761e15619781ba4
    UserName = models.CharField(max_length=20)
    PassWord = models.CharField(max_length=20)
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
    Content = models.charField()
    ReleaseTime = models.TimeField(auto_created=True)
    StartTime = models.TimeField()
    EndTime = models.TimeField()

    def __str__(self):
        return self.Title
