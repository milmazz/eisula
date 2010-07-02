from django.contrib import admin
from eisula.faq.models import Faq

class FaqAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('question',)} 

admin.site.register(Faq, FaqAdmin)
