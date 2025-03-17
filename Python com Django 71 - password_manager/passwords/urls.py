from django.urls import path
from .views import home, create_folder, folder_detail, add_password, edit_folder, delete_folder, delete_password, edit_password

urlpatterns = [
    path('', home, name='home'),
    path('create_folder/', create_folder, name='create_folder'),
    path('folder/<int:folder_id>/', folder_detail, name='folder_detail'),
    path('folder/<int:folder_id>/add_password/', add_password, name='add_password'),
    path('folder/edit/<int:folder_id>/', edit_folder, name='edit_folder'),
    path('folder/delete/<int:folder_id>/', delete_folder, name='delete_folder'),
    path('password/edit/<int:entry_id>/', edit_password, name='edit_password'),
    path('password/delete/<int:entry_id>/', delete_password, name='delete_password'),
]
