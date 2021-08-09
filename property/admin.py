from django.contrib import admin

from .models import Claim, Flat, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ("owner",)


class FlatAdmin(admin.ModelAdmin):
    raw_id_fields = ("liked_by",)
    search_fields = ('owner', 'town', 'address', )
    readonly_fields = ["created_at"]
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    inlines = [OwnerInline]


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat", 'who_complained')
    list_display = ['who_complained', 'flat']
    list_filter = ['who_complained']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat",)
    list_display = ['owner', 'owner_pure_phone']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)


