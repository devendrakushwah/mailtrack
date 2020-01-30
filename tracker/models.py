from django.db import models


class Email(models.Model):
    created_at = models.TextField(max_length=1000)
    subject = models.TextField(max_length=1000)

    def __str__(self):
        return self.subject


class TrackingInfo(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    ip = models.TextField(max_length=1000)
    details = models.TextField(max_length=10000)
    date = models.TextField(max_length=1000)

    def __str__(self):
        return self.email.subject + ' : ' + str(self.id)
