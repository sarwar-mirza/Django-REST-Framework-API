'''
Note:
JWT install - pip install djangorestframework-simplejwt
HTTP install- pip install httpie

Generate token guidelines:
1st- http POST http://127.0.0.1:8000/gettoken/ username="user1" password="sarwarmithu"
2nd(Optional)- http POST http://127.0.0.1:8000/verifytoken/ token="provide_access_token_serial_number"
3rd - http POSt http://127.0.0.1:8000/refreshtoken/ refresh="provide_access_refresh_serial_number" 

Access token guidlines:
1st- any command prompt open
2nd- without authentication and permission for rest_framework, http http://127.0.0.1:8000/urls
            Ex- http http://127.0.0.1:8000/studentapi/ 


1st- any command prompt open
2nd- with atuthentication and permission for rest_framework, http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer create_token_serial_number'
                Ex- http http://127.0.0.1:8000/studentapi/ 'Authorization:Bearer 5c8aea9fe205e5759cdedbea6058de229898c093'
    
    1st - any command prompt open
    2nd - with atuthentication and permission for (POST,PUT,DELETE)rest_framework, 
        Ex-
        post->    http -f POST http://127.0.0.1:8000/studentapi/ name=sarwar roll=104 city=Noakhali'Authorization:Bearer access_token_serial_number'
        put->     http PUT http://127.0.0.1:8000/studentapi/4/ name=mithu roll=104 city=Noakhali'Authorization:Bearer access_token_serial_number'
        delete->  http DELETE http://127.0.0.1:8000/studentapi/4/ 'Authorization:Bearer access_token_serial_number'
'''






from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api import views

# Create Router
router = DefaultRouter()

# Register StudentModelViewSet with router

router.register('studentapi', views.StudentModelViewSet, basename='student')

# (JWT)-JSON WEB TOKEN
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),      # Define Authenticattion user
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),         # refresh authentication time consuming task
    path('verifytoken/', TokenVerifyView.as_view(), name='verify_token'),
]
