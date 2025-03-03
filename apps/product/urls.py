from django.urls import path
from apps.product.views import (ProductCreateAPIView, ProductListAPIView,
                                ProductDetailAPIView, ProductDeleteAPIView,
                                ProductUpdateAPIView)

urlpatterns = [
    path("product/", ProductListAPIView.as_view(), name='product'),
    path('product/create', ProductCreateAPIView.as_view(), name="product_create"),
    path("product/<slug:slug>/", ProductDetailAPIView.as_view(), name='product_detail'),
    path("product/<slug:slug>/update", ProductUpdateAPIView.as_view(), name='product_update'),
    path("product/<slug:slug>/delete", ProductDeleteAPIView.as_view(), name='product_delete')
]
