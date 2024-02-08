from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView

app_name = "core"

urlpatterns = [
    #INICIO
    path("", views.index, name="index"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name='core/logout.html'), name="logout"),
    path("register/", views.Register.as_view(), name="register"),
    path("about/", TemplateView.as_view(template_name="core/about.html"), name="about"),
    #TOPS
    path("producto/list/tops/", views.ProductoListTops.as_view(), name="producto_list_tops"),
    path("producto/update/tops/<int:pk>", views.ProductoUpdateTops.as_view(), name="producto_update_tops"),
    path("producto/detail/tops/<int:pk>", views.ProductoDetailTops.as_view(), name="producto_detail_tops"),
    path("producto/delete/tops/<int:pk>", views.ProductoDeleteTops.as_view(), name="producto_delete_tops"),
    #JEANS
    path("producto/list/jeans/", views.ProductoListJeans.as_view(), name="producto_list_jeans"),
    path("producto/update/jeans/<int:pk>", views.ProductoUpdateJeans.as_view(), name="producto_update_jeans"),
    path("producto/detail/jeans/<int:pk>", views.ProductoDetailJeans.as_view(), name="producto_detail_jeans"),
    path("producto/delete/jeans/<int:pk>", views.ProductoDeleteJeans.as_view(), name="producto_delete_jeans"),
    #VESTIDOS
    path("producto/list/vestidos/", views.ProductoListVestidos.as_view(), name="producto_list_vestidos"),
    path("producto/update/vestidos/<int:pk>", views.ProductoUpdateVestidos.as_view(), name="producto_update_vestidos"),
    path("producto/detail/vestidos/<int:pk>", views.ProductoDetailVestidos.as_view(), name="producto_detail_vestidos"),
    path("producto/delete/vestidos/<int:pk>", views.ProductoDeleteVestidos.as_view(), name="producto_delete_vestidos"),
]
#urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
