from django.shortcuts import  HttpResponse

from home_page_content.models import Reviews
from home_page_content.web_scraper import get_reviews
from .models import Review_scheduling, c
import time
from django.utils import timezone
def Run_review_fetch():
    if Review_scheduling.objects.order_by('-created_at').first().is_15_days_old():
        Reviews.objects.all().delete()
        reviews_data = get_reviews()
        for review_data in reviews_data:
            if int(review_data['rating']) < 4:
                pass
            else:
                Reviews.objects.create(
                    Username=review_data['username'],
                    rating=str(review_data['rating']),  # Convert to string
                    description=review_data.get('description', ''),  # Handle missing descriptions
                    date=review_data['date']
                )
        Review_scheduling.objects.create(created_at=timezone.now())
    




def cron(request):
    if request.method == "GET":
        Run_review_fetch()
        t = time.time()
        if c.objects.exists():
            obj = c.objects.first()
            obj.flag = t
            obj.save()
        else:
            new = c(flag=t)
            new.save()

        return HttpResponse(f"Woke up today at {t}")
    else:
        return HttpResponse("Invalid request")
