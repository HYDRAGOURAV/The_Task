from django.contrib import admin
from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.main_Page),
    path('add_User',views.add_User, name='add_User'),
    path('task_details',views.task_details, name='task_details'),
    path('see_task/<int:user_id>',views.see_task, name='see_task'),
]
