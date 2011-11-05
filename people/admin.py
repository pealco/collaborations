from django.contrib import admin
from people.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display        = ('name', 'status')
    
    fieldsets = (
        (None, {
            'fields': ('status', 'name', 'specialization', 'collaborators')
        }),
    )

admin.site.register(Person, PersonAdmin)
