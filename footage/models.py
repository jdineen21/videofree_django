import uuid

from django.db import models

from django.contrib.auth.models import User

class File(models.Model):
    OTHER_TAG = 'OTH'
    FOOTAGE_TAGS = [
        ('ACT', 'Action Stock'),
        ('DRN', 'Drone Stock'),
        ('LND', 'Landscapes Stock'),
        (OTHER_TAG, 'Other'),
    ]
    key = models.IntegerField(primary_key=True, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    footage_file = models.FileField(
        upload_to='footage/',
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
        verbose_name_plural = 'Files'
