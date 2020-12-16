"""importamos la libreria para poder crear la paginacion de la aplicacion"""
from  rest_framework.pagination import PageNumberPagination

"""creamos una clase para genera la paginacion"""
class StandardResultsSetPagination(PageNumberPagination):
       """generamos el minimo y el maximo de paginas en  nuestra aplicacion"""
       page_size =2
       page_size_query_param = 'page_size'
       max_page_size = 1000