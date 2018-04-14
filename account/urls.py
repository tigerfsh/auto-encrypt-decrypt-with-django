from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# api endpoints
urlpatterns = format_suffix_patterns([
    path('add_personal_data', views.AddPersonalData.as_view(), name="add-personal-data"),
    path('retrieve_personal_data', views.RetrievePersonalData.as_view(), name="retrieve-personal-data")

])
