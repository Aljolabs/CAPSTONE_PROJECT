# Django admin has been removed from this project
# This file is kept for compatibility purposes but contains no functionality

from django.contrib import admin

from core.models import *

admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(BookingInventory)
admin.site.register(Feedback)
admin.site.register(InventoryCategory)
admin.site.register(InventoryItem)
admin.site.register(InventoryTransaction)
admin.site.register(Notification)
admin.site.register(Service)
admin.site.register(StaffService)
admin.site.register(UserProfile)
