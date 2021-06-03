from django.db import models
from django.utils import timezone

# Create your models here.
class Subscriber(models.Model):
    sys_id = models.AutoField(primary_key= True)
    username_sub = models.CharField(max_length=10)
    email = models.EmailField(max_length=150, null=False , blank=True,unique= True )
    created_date = models.DateTimeField(default=timezone.now)

    
    def __str__(self):
        return self.email  
