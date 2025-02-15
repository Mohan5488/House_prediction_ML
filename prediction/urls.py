from django.urls import path
from .views import predict_home_price, home, about

urlpatterns = [
    path("", home, name="home"),
    path("about", about, name="about"), 
    path("predict_home_price", predict_home_price, name="predict_home_price"),
]
