from django.contrib import admin
from django.urls import path
from PadelApp.views import inicio, MarcaCreateView, MarcaListView, MarcaUpdateView, MarcaDeleteView,  \
    MarcaDetailView, SearchMarca ,  CircuitoCreateView, CircuitoUpdateView, CircuitoDeleteView, CircuitoDetailView, \
    CircuitoListView, SearchCircuito, JugadorCreateView, JugadorDetailView, JugadorListView, \
    JugadorUpdateView, SearchJugador, JugadorDeleteView, ComentarioCreateView, ComentarioListView, \
    ComentarioDetailView, ComentarioDeleteView, ComentarioUpdateView, SearchComentarioTitulo, SearchComentarioTexto

    
    
    
urlpatterns = [
    #URLS CLASES DE VISTA MARCAS
    path("marcas/", MarcaListView.as_view(), name="listar_marcas" ),
    path("crear_marca/", MarcaCreateView.as_view(), name="crear_marca" ),
    path("buscar_marca/", SearchMarca.as_view(), name="buscar_marca" ),
    path("borrar_marcas/<int:pk>/", MarcaDeleteView.as_view(), name="borrar_marca" ),
    path("editar_marcas/<int:pk>/", MarcaUpdateView.as_view(), name="editar_marca" ), 
    path("ver_marcas/<int:pk>/", MarcaDetailView.as_view(), name="detalle_marca" ),   
   
    #URLS DE CLASES VISTA JUGADOR
    path("jugadores/", JugadorListView.as_view(), name="listar_jugadores" ),
    path("crear_jugador/", JugadorCreateView.as_view(), name="crear_jugador" ),
    path("buscar_jugador/", SearchJugador.as_view(), name="buscar_jugador" ),
    path("borrar_jugadores/<int:pk>/", JugadorDeleteView.as_view(), name="borrar_jugador" ),
    path("editar_jugadores/<int:pk>/", JugadorUpdateView.as_view(), name="editar_jugador" ),
    path("ver_jugadores/<int:pk>/", JugadorDetailView.as_view(), name="detalle_jugador" ),
   
    #URLS DE CLASES DE VISTA
    path("circuitos/", CircuitoListView.as_view(), name="listar_circuitos" ),
    path("crear-circuitos/", CircuitoCreateView.as_view(), name="crear_circuito" ),
    path("ver-circuitos/<int:pk>/", CircuitoDetailView.as_view(), name="detalle_circuito" ),
    path("editar-circuitos/<int:pk>/", CircuitoUpdateView.as_view(), name="editar_circuito" ),
    path("borrar-circuitos/<int:pk>/", CircuitoDeleteView.as_view(), name="borrar_circuito" ),
    path("buscar-circuitos/", SearchCircuito.as_view(), name="buscar_circuito" ),
    
    #URLS DE COMENTARIOS
    path("crear_comentario/", ComentarioCreateView.as_view(), name="crear_comentario" ),
    path("listar_comentarios", ComentarioListView.as_view(), name="listar_comentarios" ),
    path("detalle_comentario/<int:pk>/", ComentarioDetailView.as_view(), name="detalle_comentario" ),
    path("editar_comentario/<int:pk>/",  ComentarioUpdateView.as_view(), name="editar_comentario" ),
    path("borrar_comentario/<int:pk>/", ComentarioDeleteView.as_view(), name="borrar_comentario" ),
    path("buscar_comentario_titulo/", SearchComentarioTitulo.as_view(), name="buscar_comentario_titulo" ),
    path("buscar_comentario_texto/", SearchComentarioTexto.as_view(), name="buscar_comentario_texto" ),
]
