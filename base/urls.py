from django.urls import path
from base.views import product_list,purchase_product,success
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [

    path('',product_list,name='product_list' ),
    path('home',product_list,name='product_list'),
    path('purchase/<int:product_id>/',purchase_product, name='purchase_product'),
    path('success',success,name='success')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)