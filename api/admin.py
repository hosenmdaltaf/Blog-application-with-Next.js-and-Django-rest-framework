from django.contrib import admin

from .models import Post,Author,Category

admin.site.register(Author)
admin.site.register(Post)
# admin.site.register(Category)

from mptt.admin import MPTTModelAdmin

# admin.site.register(Post,PostAdmin)
admin.site.register(Category , MPTTModelAdmin) 
