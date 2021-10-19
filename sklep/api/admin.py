from django.contrib import admin
from .models import OdziezMeska, OdziezDamska,TypUbraniaM,TypUbraniaK
# Register your models here.
admin.site.register(OdziezMeska)
admin.site.register(OdziezDamska)
admin.site.register(TypUbraniaM)
admin.site.register(TypUbraniaK)

