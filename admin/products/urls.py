from django.urls import path

from products.views import ProductViewset, UserAPIView

urlpatterns = [
    path('products', ProductViewset.as_view(
         {
             'get': 'list',
             'post': 'create'
         })),
         path(
             'products/<str:pk>',
             ProductViewset.as_view(
                 {
                     'get': 'retrieve',
                     'put': 'update',
                     'delete': 'destroy'
                 })),
        path('user', UserAPIView.as_view()),
]
