from django.urls import path

from .views import (
    gps_update,
    gps_latest,
    gps_dashboard
)


urlpatterns = [

    path(
        "gps/update/",
        gps_update,
        name="gps_update"
    ),

    path(
        "gps/latest/",
        gps_latest,
        name="gps_latest"
    ),
        path(
        "",
        gps_dashboard,
        name="gps_dashboard"
    ),

]