from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import job_listing  # Import your job_listing model

@require_http_methods(["GET"])
def job_listings_json_view(request):
    try:
        jobs = job_listing.objects.all().order_by('-id')  # Get all jobs, ordered by newest first
        if jobs:
            data = {
                "job_listings": [
                    {
                        "Title": job.Title,
                        "Required_skills": [skill.skill for skill in job.Required_skills.all()],
                        "Experience_level": job.Experience_level,
                        "Employment_type": job.Employment_type,
                        "Work_Mode": job.Work_Mode,
                        "Job_Location": job.Job_Location,
                        "Years_of_Experience_Required": job.Years_of_Experience_Required,
                        "Salary_Range": job.Salary_Range,
                        "Educational_Qualifications": job.Educational_Qualifications,
                        "Certifications": job.Certifications,
                        "Other_Benefits": job.Other_Benefits,
                        "Number_of_Openings": job.Number_of_Openings,
                        "Client_Name": job.Client_Name,
                        "Client_Industry": job.Client_Industry,
                        "Job_Description": str(job.Job_Description),  # Convert HTMLField to string
                        "Questions": str(job.Questions)  # Convert HTMLField to string
                    } 
                    for job in jobs
                ]
            }
        else:
            data = {"error": "No job listings found."}
    except Exception as e:
        data = {"error": str(e)}
    return JsonResponse(data, safe=False)  # safe=False for array serialization