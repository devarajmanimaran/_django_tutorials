# from django.urls import path
# from .views import index  # Import your views


# urlpatterns = [
#     path("", index, name="home"),
# ]

from django.urls import path
from .views import home_view

urlpatterns = [
    path("", home_view, name="home"),
]
