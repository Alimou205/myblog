from django.contrib import admin
from .models import Category,Comment, Post

# Register your models here.
admin.site.register(Category)
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display =('title','status','created','published','author')
    prepopulated_fields ={'slug':('title',)}
    search_fields = ('title','body')
    ordering=('author','status','published')
    list_filter=('author','created','published')
@admin.register(Comment)
class Comments(admin.ModelAdmin):
    list_display =['username','email','created']