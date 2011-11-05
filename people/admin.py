from django.contrib import admin
from people.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display        = ('full_name', 'status')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    
    fieldsets = (
        (None, {
            'fields': ('status', ('first_name', 'last_name'), 'title', 'specialization', 'url', 'email', 'office', 'phone', 'collaborators')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug', 'is_alum', 'is_active',)
        }),
    )

admin.site.register(Person, PersonAdmin)
