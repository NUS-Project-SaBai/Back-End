from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path("medications", views.MedicationView.as_view()),
    path("medications/<int:pk>", views.MedicationView.as_view()),
    path("vitals", views.VitalsView.as_view()),
    path("vitals/<int:pk>", views.VitalsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
