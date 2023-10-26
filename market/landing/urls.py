from django.urls import path
from . import views
urlpatterns = [
    path('',views.LandingDashboard.as_view(),name='landing_dashboard'),
    path('dashboard/',views.LandingDashboard.as_view(),name='landing_dashboard'),
    path('order-placed/',views.OrderPlaced.as_view(),name='order-placed'),
    path('phone_pay_web/',views.webhook_handel,name='phone_pay_web'),
]
