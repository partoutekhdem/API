from django.contrib import admin
from .models import Order, Offer, PrivacyPolicy, UserCall, ChauffeurCall



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["__str__", "status"]
    list_filter = ["status"]
    def has_add_permission(self, request) -> bool:
        return False
    
    def has_change_permission(self, request, obj = None) -> bool:
        return False
    

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    def has_add_permission(self, request) -> bool:
        return False
    
    def has_change_permission(self, request, obj = None) -> bool:
        return False


admin.site.register(PrivacyPolicy)
admin.site.register(UserCall)
admin.site.register(ChauffeurCall)