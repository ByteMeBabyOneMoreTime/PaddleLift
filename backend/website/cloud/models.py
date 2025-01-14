from django.db import models


class CV(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, default='default@example.com')
    phone_no = models.CharField(max_length=255, default='000000000000')

    cv_url = models.URLField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "CV"
        verbose_name_plural = "CVs"

    def __str__(self):
        return self.name