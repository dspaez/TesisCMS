from django.contrib import admin

from .models import MonumentosQuito

admin.site.register(MonumentosQuito)
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)