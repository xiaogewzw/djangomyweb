from django.db import models


class User(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    creation_time = models.DateTimeField()

    def __str__(self):
        return self.username

class Message(models.Model):
    message_user = models.CharField(max_length = 20)
    message_text = models.CharField(max_length = 20)
    message_contect = models.CharField(max_length = 100)
    message_time = models.DateTimeField()

    def __str__(self):
        return self.message_text

