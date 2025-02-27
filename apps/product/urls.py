from django.urls import path
from apps.product.views import (ProductCreateAPIView, ProductListAPIView,
                                ProductDetailAPIView, ProductDeleteAPIView,
                                ProductUpdateAPIView)

urlpatterns = [
    path("product/", ProductListAPIView.as_view(), name='product'),
    path('product/create', ProductCreateAPIView.as_view(), name="product_create"),
    path("product/<slug:slug>/", ProductDetailAPIView.as_view(), name='product_detail'),
    path("product/<int:pk>/update", ProductUpdateAPIView.as_view(), name='product_update'),
    path("product/<int:pk>/delete", ProductDeleteAPIView.as_view(), name='product_delete')
]
