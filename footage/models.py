from django.db import models

class Footage(models.Model):
    OTHER_TAG = 'OTH'
    FOOTAGE_TAGS = [
        ('ACT', 'Action Stock'),
        ('DRN', 'Drone Stock'),
        ('LND', 'Landscapes Stock'),
        (OTHER_TAG, 'Other'),
    ]
    title = models.CharField(max_length=50)
    upload_datetime = models.DateTimeField()
    tags = models.CharField(
        max_length=3,
        choices=FOOTAGE_TAGS,
        default=OTHER_TAG,
    )
    description = models.TextField()
