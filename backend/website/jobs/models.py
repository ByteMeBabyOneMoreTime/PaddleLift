from django.db import models
from tinymce.models import HTMLField

class currency(models.Model):
    sign = models.CharField(verbose_name="Currency", max_length=400)
    
    def __str__(self):
        return self.sign

class job_listing(models.Model):
    Title = models.CharField(verbose_name="Title",max_length=500, null=False, blank=False)
    Recruiter_email = models.EmailField(max_length=2000)
    Required_skills = models.TextField(verbose_name="Required Skills", help_text="differentiate with a comma. example object1, object2",blank=False)
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
    Experience_level = models.CharField(verbose_name="Experience Level",max_length=300, choices=Experience_Level_Choices, blank=True, default="")
    Employment_type = models.CharField(verbose_name="Employment type",max_length=300, choices=Employment_Type_Choices, default="Full-Time")
    Work_Mode_Choices = (
        ('On-site', 'On-site'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid')
    )
    Work_Mode = models.CharField(verbose_name="Work Mode",max_length=300, choices=Work_Mode_Choices, default="On-site")
    Job_Location = models.CharField(verbose_name="Job Location",max_length=2000, blank=False, null=False)
    Min_Years_of_Experience_Required = models.PositiveIntegerField(verbose_name="Min Years of Experience", help_text="only positive integers allowed")
    Max_Years_of_Experience_Required = models.PositiveIntegerField(verbose_name="Max Years of Experience", help_text="only positive integers allowed")
    Currency = models.ForeignKey(currency, on_delete=models.PROTECT)
    Min_Salary= models.PositiveIntegerField(verbose_name="Min Salary", help_text="only positive integers allowed")
    Max_Salary= models.PositiveIntegerField(verbose_name="Max Salary", help_text="only positive integers allowed")
    Educational_Qualifications = models.CharField(verbose_name="Education Qualifications", help_text="differentiate with a comma. example object1, object2", max_length=2000, blank=True, null=True, default="")
    Certifications = models.TextField(verbose_name="Certifications", help_text="differentiate with a comma. example object1, object2", blank=True, null=True, default="")
    Other_Benefits = models.CharField(verbose_name="Other Benefits",max_length=2000, blank=True, null=True, default="")
    Number_of_Openings = models.PositiveIntegerField(verbose_name="Number of Openings", default=0, help_text="only positive integers allowed")
    Client_Name = models.CharField(verbose_name="Client Name",max_length=2000, blank=True, null=True, default="")
    Client_Industry = models.CharField(verbose_name="Client Industry",max_length=2000, blank=False, null=False)
    Job_Description = HTMLField(verbose_name="Job Description")
    Questions = models.TextField(verbose_name="Questions",help_text="Add all the Questions to be answered by the candidate. differentiate with a comma. example object1, object2", default="")
