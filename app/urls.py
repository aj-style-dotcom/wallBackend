from django.urls import path
from . import views

urlpatterns=[
  path("cate", views.getCatego),
  path("all", views.getAll),
  path("wall/<int:id>", views.get_by_id),
  path("wall/<str:cate>", views.get_by_cate),
  
  ]