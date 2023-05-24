from django.contrib import admin

# Register your models here.
from products.models import User, Glav, Roman, Block, Stix, Sobit, Resens

admin.site.register(User)
admin.site.register(Glav)
admin.site.register(Roman)
admin.site.register(Block)
admin.site.register(Stix)
# admin.site.register(Tag)
admin.site.register(Sobit)
admin.site.register(Resens)