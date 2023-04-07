from django.urls import path
from app import views

urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('update/<pk>/',views.update.as_view(),name='update'),
    path('delete/<pk>/',views.delete.as_view(),name='delete'),
]
