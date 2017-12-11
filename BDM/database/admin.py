from django.contrib import admin

# Register your models here.
from .models import (WorkEnt,
                     WorkAttrib,
                     )

admin.site.register(WorkEnt)
admin.site.register(WorkAttrib)
