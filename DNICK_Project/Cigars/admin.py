from django.contrib import admin
from django.contrib import admin
from .models import Kupuvac, Proizvoditel, Proizvod, Prodavac, ProdavacProizvod, KupuvacProizvod, Najava
class ProdavacProizvodAdmin(admin.TabularInline):
    model= ProdavacProizvod
    extra = 0
    fk_name ="Prodavac"

class KupvacProizvodAdmin(admin.TabularInline):
    model= KupuvacProizvod
    extra = 0
    fk_name ="Kupuvac"

class KupuvacAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        self=request.user
        return super().save_model(request,obj,form,change)
    def has_change_permission(self, request, obj=None):

        if(self) and (request.user==self):
            return True
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    list_display = ('Ime', 'Prezime', 'Username', 'godina_na_ragjane')
    list_filter = ('Ime', 'Prezime', 'Username')
    search_fields = ('Ime', 'Prezime', 'Username')

class ProdavacAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        self=request.user
        return super().save_model(request,obj,form,change)
    def has_change_permission(self, request, obj=None):

        if(self) and (request.user==obj.user):
            return True
        return False
    def has_delete_permission(self, request, obj=None):
        return False

    list_display = ('sifra', 'ime_na_proizvoditel', 'cena', 'zaliha')
    list_filter = ('ime_na_proizvoditel', 'zemja_na_poteklo')
    search_fields = ('ime_na_proizvoditel', 'zemja_na_poteklo')
# Register your models here.


admin.site.register(Kupuvac)
admin.site.register(Proizvoditel)
admin.site.register(Proizvod)
admin.site.register(Prodavac)
admin.site.register(ProdavacProizvod)
admin.site.register(KupuvacProizvod)
admin.site.register(Najava)