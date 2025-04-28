from django.contrib import admin
from .models import Room, RoomImage

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1
class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 2
class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 3
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]

admin.site.register(Room, RoomAdmin)
admin.site.register(RoomImage)
