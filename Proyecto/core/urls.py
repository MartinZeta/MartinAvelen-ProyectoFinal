from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("producto/list/tops/", views.ProductoListTops.as_view(), name="producto_list_tops"),
    path("producto/list/jeans/", views.ProductoListJeans.as_view(), name="producto_list_jeans"),
    path("producto/list/vestidos/", views.ProductoListVestidos.as_view(), name="producto_list_vestidos"),
    path("producto/update/tops/<int:pk>", views.ProductoUpdateTops.as_view(), name="producto_update_tops"),
    
]
#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
