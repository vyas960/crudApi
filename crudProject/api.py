from rest_framework import routers
from testApp import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewset)
