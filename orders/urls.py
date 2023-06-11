from django.urls import path
from . import views



urlpatterns = [
    path('saveDataOrder/', views.save_date_order),
    path('getOrderByTypeVehicle/', views.get_order_by_type_vehicle),
    path('getOrders/', views.get_orders),
    path('getOffersByOrders/', views.get_offers_by_orders),
    path('uploadImageBay/', views.upload_image_bay),
    path('getOrdersCanceled/', views.get_orders_canceled),
    path('getOrdersStartFinish/', views.get_orders_start_finish),
    path('getOrdersStartDone/', views.get_orders_start_done),
    path('getOrdersNormal/', views.get_orders_normal),
    path('getOrdersStart/', views.get_orders_start),
    path('getAllClient/', views.get_all_client),
    path('getAllDrivers/', views.get_all_drivers),
    path('updateClient/', views.update_client),
    path('updateDriver/', views.update_driver),
    path('getDriverOld/', views.get_driver_old),
    path('getDriverOldNotSubscribe/', views.get_driver_old_not_subscribe),
    path('getDriverNew/', views.get_driver_new),
    path('getDriverBanned/', views.get_driver_banned),
    path('getDriverReject/', views.get_driver_reject),
    path('getPrivacyPolicy/', views.get_privacy_policy),
    path('getRide/', views.get_ride),
    path('updateRide/', views.update_order),
    path('updateRatingChauffeur/', views.update_rating_chauffeur),
    path('addOffer/', views.add_offer),
    path('deleteOffer/', views.delete_offer),
    path('getCallsUser/', views.get_call_user),
    path('getCallsChauffeur/', views.get_call_chauffeur)
]
