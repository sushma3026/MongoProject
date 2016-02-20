from django.contrib import admin

from .models import item


class ItemAdmin(admin.ModelAdmin):
	list_display = ['title','amount']

admin.site.register(item, ItemAdmin)



