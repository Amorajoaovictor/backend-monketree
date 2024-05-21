from django.contrib import admin
from .models import User
from .models import Block
from .models import Click
from .models import Tree
# Register your models here.
admin.site.register(User)
admin.site.register(Block)
admin.site.register(Click)


class TreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'link')


admin.site.register(Tree, TreeAdmin)

