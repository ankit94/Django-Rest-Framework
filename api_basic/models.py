from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=20)
    groups = models.ManyToManyField('Group', through='Membership')


class Group(models.Model):
    name = models.CharField(max_length=20)


class Membership(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    join_date = models.DateTimeField()
