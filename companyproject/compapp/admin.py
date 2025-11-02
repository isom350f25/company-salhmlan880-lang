from django.contrib import admin
from .models import employee


# Register your models here.
@admin.register(employee)

class employeeAdmin(admin.ModelAdmin):
    list_display=('name','position','joined_on','phone_number')
    search_fields = ('name','position')
    list_filter=('joined_on',)
    pass
    

