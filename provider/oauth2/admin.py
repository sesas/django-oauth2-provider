from django.contrib import admin
from .models import AccessToken, Grant, Client, RefreshToken


class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'token', 'expires', 'scope',)
    raw_id_fields = ('user',)


class GrantAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'code', 'expires',)
    raw_id_fields = ('user',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_auto_approved', 'url', 'user', 'redirect_uri', 'client_id', 'client_type', 'approval_type')
    list_display_links = ('name', 'url', 'client_id')
    list_filter = ('client_type', 'approval_type')
    search_fields = ('name', 'url', 'redirect_uri', 'client_id', 'client_type')
    raw_id_fields = ('user',)
    readonly_fields = ('client_id', 'client_secret')


admin.site.register(AccessToken, AccessTokenAdmin)
admin.site.register(Grant, GrantAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(RefreshToken)
