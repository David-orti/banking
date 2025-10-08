from django.contrib import admin
from .models import Country, Department, City, User



#  Registrar Country con una clase personalizada
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abrev', 'get_status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('name', 'abrev')

    def get_status(self, obj):
        return "Active" if obj.status else "Inactive"
    get_status.short_description = 'Status'  # etiqueta de la columna


#  Registrar los demás modelos (básico)
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abrev', 'country', 'status')
    list_filter = ('status', 'country')
    search_fields = ('name', 'abrev')



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'abrev', 'department', 'status')
    list_filter = ('status', 'department')
    search_fields = ('name', 'abrev')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'email', 'city', 'status')
    list_filter = ('status', 'city')
    search_fields = ('firstname', 'lastname', 'email')

    

