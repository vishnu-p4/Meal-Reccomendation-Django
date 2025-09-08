from django.urls import path
from meals import views


urlpatterns = [

    path('',views.register , name = 'register'),
    path('home',views.home , name  = 'home'),
    path('meal_recommendations/', views.meal_recommendations, name='meal_recommendations'),
    
]