from django.urls import path
from .views import index


app_name = "companyinfo"

urlpatterns = [
    path("", index, name="index"),
]
