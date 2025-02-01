from django.db import models

# Create your models here.
from django.db import models

class FaceSwapImage(models.Model):
    source_image = models.ImageField(upload_to="uploads/")
    target_image = models.ImageField(upload_to="uploads/")
    output_image = models.ImageField(upload_to="outputs/", blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
