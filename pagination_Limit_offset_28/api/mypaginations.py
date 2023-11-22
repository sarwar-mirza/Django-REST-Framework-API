from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    
   default_limit = 4
   
   '''
   limit_query_param = 'mylimit'      # Custom name lamit search in urls 
   offset_query_param = 'myoffset'    # "offset" query parameter. starting point in database and custom name offset in urls
   max_limit = 6                      # If set this is a numeric value indicating the maximum allowable limit that may be requested by the client

'''


