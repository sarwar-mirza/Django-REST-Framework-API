from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    
    page_size = 4                        # A numeric value indicating the page size
    
    
    
    '''
    page_query_param = 'p'                # A string value indicating the name of the "limit" query parameter.
    page_size_query_param = 'records'     #  this is a string value indicating the name of a query parameter that allows the client to set the page size on a per-request basis. 
    max_page_size = 7                     # If set, this is a numeric value indicating the maximum allowable requested page size. This attribute is only valid if page_size_query_param is also set.
    '''



