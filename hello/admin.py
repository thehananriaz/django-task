from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_cat', 'publish_date' ,'user']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name', 'song_duration', 'sung_by']
    
@admin.register(ExamCenter)
class ExamcenterAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'center_name', 'city']

@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'center_name', 'city']
    ordering = ['id']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email' ,'address']

