from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view()),
    
    # Susu Hewani dan Telur
    path('sensor/suhu', views.SuhuView.as_view()),
    path('sensor/kelembaban', views.KelembabanView.as_view()),
    path('sensor/cahaya', views.CahayaView.as_view()),
    path('actuator/', views.AirPurifierView.as_view()),
]
