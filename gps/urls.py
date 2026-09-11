from django.urls import path

from .views import gps_update


urlpatterns = [

    path(
        "api/gps/update/",
        gps_update,
        name="gps_update"
    ),

]