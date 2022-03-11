from django.db import models

# Create your models here.

catego=(("sea side", "sea side"), ("beach", "beach"))

class wallpeps(models.Model):
  name=models.CharField(max_length=50)
  decription=models.TextField()
  image=models.FileField(upload_to="images/")
  category=models.CharField(max_length=30, choices=catego, null=True, blank=True)
  
  def __str__(self):
    return self.name