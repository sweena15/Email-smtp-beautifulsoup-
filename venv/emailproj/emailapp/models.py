from django.db import models

# Create your models here.

class Email(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sender = models.EmailField()
    recipient = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email to {self.recipient} with subject '{self.subject}'"

class LinkClick(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    url = models.URLField()
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Link {self.url} clicked {self.click_count} times for email '{self.email.subject}'"
