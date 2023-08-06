from django.db import models

class leaveAReview(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True)
    school_name = models.CharField(max_length=100, blank=True)
    year_group = models.CharField(max_length=10, blank=True)
    predicted_grade = models.CharField(max_length=5, blank=True)
    achieved_grade = models.CharField(max_length=5, blank=True)
    star_rating = models.IntegerField(blank=True)
    feedback_comments = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    passcode = models.CharField(max_length=20, blank=True)
    # Add other fields as needed

class leaveAReviewText(models.Model):
    intro_text = models.TextField(max_length=800)