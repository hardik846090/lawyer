from django.contrib import admin
from .models import Services, Practices, Contact, Law, Media, MediaComment, Consulation

# Register your models here.

admin.site.register(Services)
admin.site.register(Practices)
admin.site.register(Contact)
admin.site.register(Law)
admin.site.register(Media)
admin.site.register(MediaComment)
admin.site.register(Consulation)
