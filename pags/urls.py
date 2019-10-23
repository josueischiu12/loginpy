from django.urls import path

from . import views

app_name = "pags"

urlpatterns = [
    path("", views.home, name="home"),
    path("pagina/", views.PaginaListView.as_view(), name="lista"),
    path("pagina/<int:pk>/", views.PaginaDetailView.as_view(), name="detalle"),
    path("pagina/nueva/", views.PaginaCreateView.as_view(), name="nuevo"),
    path("pagina/editar/<int:pk>/", views.PaginaUpdateView.as_view(), name="editar"),
    path("pagina/borrar/<int:pk>/", views.PaginaDeleteView.as_view(), name="borrar"),
]