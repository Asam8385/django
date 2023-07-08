from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("book", views.book, name="book"),
    path("", views.index, name="index"),
    path("reserve", views.Reserve, name="reserve"),
    path("bookings", views.bookings_api, name="bookings"),
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)