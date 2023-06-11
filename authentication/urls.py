from django.urls import path
from . import views

urlpatterns = [
    path('sendCode/', views.send_code),
    path('checkCode/', views.check_code),
    path('saveDataClient/', views.save_date_client),
    path('saveDataDriver/', views.save_date_driver),
    path('getDataUser/', views.get_data_user),
]
