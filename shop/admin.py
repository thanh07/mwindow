from django.contrib import admin
from .models import Color, Profile, Aluminium
# Register your models here.

class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Color, ColorAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Profile, ProfileAdmin)

class AluminiumAdmin(admin.ModelAdmin):
    list_display = ['name', 'code','slug','description', 'leng','change','created','updated']
    list_filter = ['code','created', 'updated']
    list_editable = ['change',]
    prepopulated_fields = {'slug': ('code',)}
admin.site.register(Aluminium, AluminiumAdmin)
