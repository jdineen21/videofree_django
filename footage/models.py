import uuid

from django.db import models

from django.contrib.auth.models import User

class Footage(models.Model):
    OTHER_TAG = 'OTH'
    FOOTAGE_TAGS = [
        ('ACT', 'Action Stock'),
        ('DRN', 'Drone Stock'),
        ('LND', 'Landscapes Stock'),
        (OTHER_TAG, 'Other'),
    ]
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    file_loc = models.CharField(
        verbose_name='File Location',
        max_length=100,
    )
    upload_datetime = models.DateTimeField(
        auto_now_add=True,
    )
    tags = models.CharField(
        max_length=3,
        choices=FOOTAGE_TAGS,
        default=OTHER_TAG,
    )
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Footage'
