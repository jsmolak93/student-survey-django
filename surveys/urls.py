from django.urls import path
from . import views

urlpatterns = [
    path('surveys/', views.get_all_surveys),
    path('surveys/<int:id>/', views.get_survey_by_id),
    path('surveys/create/', views.create_survey),
    path('surveys/update/<int:id>/', views.update_survey),
    path('surveys/delete/<int:id>/', views.delete_survey),
]
