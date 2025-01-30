from django.db import models
from tinymce.models import HTMLField

class skill(models.Model):
    skill = models.CharField(max_length=500, null=False, blank=False)
    def __str__(self):
        return str(self.skill)

class job_listing(models.Model):
    Title = models.CharField(max_length=500, null=False, blank=False)
    Required_skills = models.ManyToManyField(skill, related_name='job_listings')
    Experience_Level_Choices = (
        ('Entry-level', 'Entry-level'),
        ('Mid-level', 'Mid-level'),
        ('Senior-level', 'Senior-level'),
        ('Manager', 'Manager'),
        ('Leadership / CXO', 'Leadership / CXO')
    )
    Employment_Type_Choices = (
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance')
    )
    Experience_level = models.CharField(max_length=300, choices=Experience_Level_Choices, blank=True, default="None")
    Employment_type = models.CharField(max_length=300, choices=Employment_Type_Choices, default="Full-Time")
    Work_Mode_Choices = (
        ('On-site', 'On-site'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid')
    )
    Work_Mode = models.CharField(max_length=300, choices=Work_Mode_Choices, default="On-site")
    Job_Location = models.CharField(max_length=2000, blank=False, null=False)
    Years_of_Experience_Required = models.IntegerField()
    Salary_Range = models.CharField(max_length=2000, blank=True, null=True, default="None")
    Educational_Qualifications = models.CharField(max_length=2000, blank=True, null=True, default="None")
    Certifications = models.CharField(max_length=2000, blank=True, null=True, default="None")
    Other_Benefits = models.CharField(max_length=2000, blank=True, null=True, default="None")
    Number_of_Openings = models.IntegerField(blank=True, default=-1)
    Client_Name = models.CharField(max_length=2000, blank=True, null=True, default="None")
    Client_Industry = models.CharField(max_length=2000, blank=False, null=False)
    Job_Description = HTMLField()
    Questions = models.TextField(help_text="Add all the Questions to be answered by the candidate", default="")
