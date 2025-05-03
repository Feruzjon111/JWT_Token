from django.urls import path
from .views import CreateAPIView, ProductListAPIView, DetailAPIView, UpdateAPIView, DeleteAPIView

urlpatterns = [
    path('create/', CreateAPIView.as_view(), name='create'),
    path('products/', ProductListAPIView.as_view(), name='list'),
    path('products/<int:pk>/', DetailAPIView.as_view(), name='detail'),
    path('products/<int:pk>/update/', UpdateAPIView.as_view(), name='update'),
    path('products/<int:pk>/delete/', DeleteAPIView.as_view(), name='delete'),
]
