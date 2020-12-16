#importamos la libreria
from  rest_framework.pagination import PageNumberPagination

#creamos una clase para generar la paginacion
class StandardResultsSetPagination(PageNumberPagination):
       page_size =2
       page_size_query_param = 'page_size'
       max_page_size = 1000