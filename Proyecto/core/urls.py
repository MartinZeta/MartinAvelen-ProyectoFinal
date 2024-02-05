from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("profesor/list/", views.profesor_list, name="profesor_list"),
    path("estudiante/list/", views.estudiante_list, name="estudiante_list"),
    path("profesor/create/", views.profesor_create, name="profesor_create"),
    path("estudiante/create/", views.estudiante_create, name="estudiante_create"),
    path("curso/list/", views.curso_list, name="curso_list"),
    path("curso/create/", views.curso_create, name="curso_create"),
    path("producto/list/tops/", views.ProductoListTops.as_view(), name="producto_list_tops"),
    
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
