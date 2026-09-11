import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import GPSLocation


def gps_dashboard(request):

    return render(
        request,
        "gps/dashboard.html"
    )

@csrf_exempt
def gps_update(request):

    if request.method != "POST":

        return JsonResponse(
            {
                "success": False,
                "message": "POST request required"
            },
            status=405
        )

    try:

        data = json.loads(
            request.body.decode("utf-8")
        )

    except json.JSONDecodeError:

        return JsonResponse(
            {
                "success": False,
                "message": "Invalid JSON"
            },
            status=400
        )

    latitude = data.get("latitude")
    longitude = data.get("longitude")

    satellites = data.get(
        "satellites",
        0
    )

    gps_valid = data.get(
        "gps_valid",
        False
    )

    rssi = data.get(
        "rssi",
        0
    )

    snr = data.get(
        "snr",
        0
    )

    if latitude is None:

        return JsonResponse(
            {
                "success": False,
                "message": "Latitude is required"
            },
            status=400
        )

    if longitude is None:

        return JsonResponse(
            {
                "success": False,
                "message": "Longitude is required"
            },
            status=400
        )

    try:

        location = GPSLocation.objects.create(

            latitude=latitude,

            longitude=longitude,

            satellites=satellites,

            gps_valid=gps_valid,

            rssi=rssi,

            snr=snr
        )

    except Exception as e:

        return JsonResponse(
            {
                "success": False,
                "message": str(e)
            },
            status=500
        )

    return JsonResponse(
        {
            "success": True,
            "message": "GPS data received",

            "id": location.id,

            "latitude": float(
                location.latitude
            ),

            "longitude": float(
                location.longitude
            ),

            "satellites": location.satellites,

            "gps_valid": location.gps_valid,

            "rssi": location.rssi,

            "snr": location.snr,

            "created_at": (
                location.created_at.isoformat()
            )
        },
        status=201
    )


# =========================================================
# LATEST GPS
# =========================================================

def gps_latest(request):

    if request.method != "GET":

        return JsonResponse(
            {
                "success": False,
                "message": "GET request required"
            },
            status=405
        )

    location = (
        GPSLocation.objects
        .order_by("-created_at")
        .first()
    )

    if location is None:

        return JsonResponse(
            {
                "success": True,
                "available": False,
                "message": "No GPS data available"
            }
        )

    return JsonResponse(
        {
            "success": True,
            "available": True,

            "id": location.id,

            "latitude": float(
                location.latitude
            ),

            "longitude": float(
                location.longitude
            ),

            "satellites": location.satellites,

            "gps_valid": location.gps_valid,

            "rssi": location.rssi,

            "snr": location.snr,

            "created_at": (
                location.created_at.isoformat()
            )
        }
    )