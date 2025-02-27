from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import job_listing  # Import your job_listing model

def safe_split(value):
    """Safely split a comma-separated string into a list, handling None and empty values properly."""
    return [x.strip() for x in value.strip().split(',') if x.strip()] if value else []

def safe_split2(value):
    """Safely split a comma-separated string into a list, handling None and empty values properly."""
    return [x.strip() for x in value.strip().split('||') if x.strip()] if value else []

@require_http_methods(["GET"])
def job_listings_json_view(request):
    try:
        jobs = job_listing.objects.all().order_by('-id')  # Get all jobs, ordered by newest first
        if jobs:
            data = {
                "job_listings": [
                    {
                        "Title": job.Title or "",  # Ensure non-null string
                        "Required_skills": safe_split(job.Required_skills),
                        "Experience_level": job.Experience_level or "",
                        "Employment_type": job.Employment_type or "",
                        "Work_Mode": job.Work_Mode or "",
                        "Job_Location": job.Job_Location or "",
                        "Years_of_Experience_Required": [
                            job.Min_Years_of_Experience_Required if job.Min_Years_of_Experience_Required is not None else 0, 
                            job.Max_Years_of_Experience_Required if job.Max_Years_of_Experience_Required is not None else 0
                        ],
                        "Currency" : job.Salary_currency,
                        "Salary_Range": [
                            job.Min_Salary if job.Min_Salary is not None else 0, 
                            job.Max_Salary if job.Max_Salary is not None else 0
                        ],
                        "Educational_Qualifications": safe_split(job.Educational_Qualifications),
                        "Certifications": safe_split(job.Certifications),
                        "Other_Benefits": job.Other_Benefits or "",
                        "Number_of_Openings": job.Number_of_Openings if job.Number_of_Openings is not None else 0,
                        "Client_Name": job.Client_Name or "",
                        "Client_Industry": job.Client_Industry or "",
                        "Job_Description": str(job.Job_Description) if job.Job_Description else "",
                        "Questions": safe_split2(job.Questions)
                    }
                    for job in jobs
                ]
            }
        else:
            data = {"error": "No job listings found."}
    except Exception as e:
        data = {"error": str(e)}
    return JsonResponse(data, safe=False)  # safe=False for array serialization