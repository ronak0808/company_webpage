from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


# Create your models here.
class GenralInfo(models.Model):
    company_name = models.CharField(max_length=255, default='Company')
    location = models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    open_hours=models.CharField(max_length=100,blank=True, null=True)
    video_url=models.URLField(blank=True, null=True)
    twitter_url=models.URLField(blank=True, null=True)
    facebook_url=models.URLField(blank=True, null=True)
    instagram_url=models.URLField(blank=True, null=True)
    linkding_url=models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.company_name
    
class Service(models.Model):
    icon=models.CharField(max_length=50, blank=True, null=True)
    title=models.CharField(max_length=255, unique=True)
    description=models.TextField()
    
    
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    user_image=models.CharField(max_length=255, blank=True, null=True)
    username=models.CharField(max_length=255)
    user_job_title=models.CharField(max_length=50)
    stars_count=[
          (1,'One'),
          (2,'Two'),
          (3,'Three'),
          (4,'Four'),
          (5,'Five'),
      ]
    rating_count=models.IntegerField(choices=stars_count)
    review=models.TextField()
    
    def __str__(self):
        return f"{self.username}-{self.user_job_title}"
    
    
    
class ContactFormLog(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField()
    action_time=models.DateTimeField(null=True, blank=True)
    is_success=models.BooleanField(default=False)
    is_error=models.BooleanField(default=False)
    error_message=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.email
    

class Author(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    joined_at=models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return self.first_name
    
    
    
class Blog(models.Model):
    blog_image=models.CharField(max_length=255, blank=True,null=True)
    category=models.CharField(max_length=55, blank=True, null=True)
    title=models.CharField(max_length=255)
    author=models.ForeignKey(Author,on_delete=models.PROTECT,blank=True,null=True)
    created_at=models.DateTimeField(default=timezone.now)
    content= RichTextField()  #models.TextField()
    
    def __str__(self):
        return self.title
    
    
   
    
    
    
