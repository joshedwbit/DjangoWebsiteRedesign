from django.db import models

class reviews(models.Model):
    Year_Groups = [
        ('ks3', 'KS3'),
        ('year-10', 'Year 10'),
        ('year-11', 'Year 11'),
        ('as', 'AS'),
        ('a2', 'A2'),
    ]

    Grade_List = [
        ('E','E'),
        ('D','D'),
        ('C','C'),
        ('B','B'),
        ('A','A'),
        ('A*','A*'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
    ]

    # sets name in the admin portal
    class Meta:
        verbose_name_plural = "Reviews"

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True)
    school_name = models.CharField(max_length=100, blank=True)
    year_group = models.CharField(max_length=20, choices=Year_Groups ,blank=True)
    predicted_grade = models.CharField(max_length=5, choices=Grade_List, blank=True)
    achieved_grade = models.CharField(max_length=5, choices=Grade_List, blank=True)
    star_rating = models.IntegerField(blank=True)
    feedback_comments = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    passcode = models.CharField(max_length=20, blank=True)
    # Add other fields as needed

class leaveAReviewText(models.Model):
    class Meta:
        verbose_name_plural = "Leave a review intro text"
    intro_text = models.TextField(max_length=800)
