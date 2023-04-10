from django.contrib import admin

from django.contrib import admin
from .models import Book,Activity,Category,Video,app_Question,Data_of_Category

admin.site.register(Category)
admin.site.register(Activity)
admin.site.register(Book)
admin.site.register(Video)
admin.site.register(app_Question)
admin.site.register(Data_of_Category)
