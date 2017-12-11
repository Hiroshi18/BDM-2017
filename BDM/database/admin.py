from django.contrib import admin

# Register your models here.
from .models import (WorkEnt,
                     ItemEnt,
                     ManifEnt,
                     ExprEnt,
                     )

admin.site.register(WorkEnt)
admin.site.register(ExprEnt)
admin.site.register(ManifEnt)
admin.site.register(ItemEnt)
