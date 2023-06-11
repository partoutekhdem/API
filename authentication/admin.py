from typing import Any, Dict, Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Client, Driver


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["__str__", "active"]
    list_filter = ["active"]

    def has_add_permission(self, request) -> bool:
        return False


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["__str__", "status", "subscribe", "active", "type", "available"]
    list_filter = ["status", "subscribe", "active", "type", "available"]
    change_form_template = "admin/authentication/driver/change_form.html"

    def changeform_view(self, request: HttpRequest, object_id: str = ..., form_url: str = ...,
                        extra_context: Dict[str, bool] = ...) -> Any:
        print(super().fields)
        return super().changeform_view(request, object_id, form_url, extra_context)

    def has_add_permission(self, request) -> bool:
        return False
