from django.db import models


class GPSLocation(models.Model):

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=6
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=6
    )

    satellites = models.PositiveIntegerField(
        default=0
    )

    gps_valid = models.BooleanField(
        default=False
    )

    rssi = models.IntegerField(
        default=0
    )

    snr = models.FloatField(
        default=0.0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.latitude}, "
            f"{self.longitude}"
        )