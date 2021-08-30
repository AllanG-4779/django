from django.urls import  path
from .views import Register,profile
urlpatterns = [
     path("register/",Register, name="register" ),
     path("user/profile",profile, name="user-profile" )
]
