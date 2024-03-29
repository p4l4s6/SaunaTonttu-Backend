from django.conf import settings
from django.db import models
from coreapp.base import BaseModel


# Create your models here.
class Device(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mac_address = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.mac_address


class SaunaSession(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, editable=False)
    avg_temp = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, editable=False)
    avg_humid = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, editable=False)
    avg_pressure = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, editable=False)
    calories_burned = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, editable=False)
    heartbit_increased = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, editable=False)
    blood_flow_increased = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, editable=False)


class Reading(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.ForeignKey(SaunaSession, on_delete=models.CASCADE)
    device = models.CharField(max_length=30)
    temp = models.DecimalField(max_digits=10, decimal_places=4)
    humidity = models.DecimalField(max_digits=10, decimal_places=4)
    pressure = models.DecimalField(max_digits=10, decimal_places=4)
    timestamp = models.DateTimeField()
