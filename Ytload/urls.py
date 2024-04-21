from django.urls import path
from .views import Home, Download, About, Contact

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('download/', Download, name="Download"),
    path('about/', About.as_view(), name="About"),
    path('contact/', Contact.as_view(), name="Contact"),
]