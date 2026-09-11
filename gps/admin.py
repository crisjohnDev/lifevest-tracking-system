from django.contrib import admin

from .models import GPSLocation


@admin.register(GPSLocation)
class GPSLocationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "latitude",
        "longitude",
        "satellites",
        "gps_valid",
        "rssi",
        "snr",
        "created_at",
    )

    list_filter = (
        "gps_valid",
        "created_at",
    )

    search_fields = (
        "latitude",
        "longitude",
    )

    ordering = (
        "-created_at",
    )