from django.contrib import admin
from family.models import hobbies, ubicacion
from family.models import familia_nava,  hobbies, ubicacion

# Register your models here.
admin.site.register(familia_nava)

admin.site.register(hobbies)

admin.site.register(ubicacion)


