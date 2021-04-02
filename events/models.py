from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Event(models.Model):
    event_title = models.CharField(max_length=40, blank=False)
    posted_by = models.CharField(max_length=40, blank=False)
    description = models.TextField(max_length=500, blank=False)
    location = models.TextField(max_length=255, blank=False)
    date = models.DateField('Event date (mm/dd/yyyy)', auto_now_add=False, auto_now=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
   


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # def approve_comments(self):
    #     return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.event_title


# class Comment(models.Model):
#     author = models.CharField(max_length=100)
#     post = models.ForeignKey('events.Event', related_name='comments',  on_delete=models.CASCADE,)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)

#     def approve(self):
#         self.approved_comment = True
#         self.save()

#     def get_absolute_url(self):
#         return reverse('post_list')

#     def __str__(self):
#         return self.text