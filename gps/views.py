import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import GPSLocation


@csrf_exempt
def gps_update(request):

    # =====================================================
    # ONLY POST IS ALLOWED
    # =====================================================

    if request.method != "POST":

        return JsonResponse(
            {
                "success": False,
                "message": "POST request required"
            },
            status=405
        )

    # =====================================================
    # READ JSON
    # =====================================================

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

    # =====================================================
    # GET DATA
    # =====================================================

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

    # =====================================================
    # REQUIRED DATA
    # =====================================================

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

    # =====================================================
    # SAVE GPS DATA
    # =====================================================

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

    # =====================================================
    # RESPONSE
    # =====================================================

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