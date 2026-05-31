from django.urls import path
from . import views


#app_name='home'
urlpatterns = [
      path('', views.home , name='home'),
      path('create/', views.create , name='create'),
      path('details/<int:todo_id>/' , views.details , name='details'),
      path('delete/<int:todo_id>/', views.delete_todo, name='delete'),  # Add this
      path('update/<int:todo_id>/', views.delete_todo, name='update')  # Add this
]