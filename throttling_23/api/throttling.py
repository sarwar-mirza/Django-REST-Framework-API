from rest_framework.throttling import UserRateThrottle

class MithuRateThrottle(UserRateThrottle):
    
    scope = 'mithu'                        # many class use in throttling individual class activity




'''
class SarwarRateThrottle(UserRateThrottle):
    
    scope = 'sarwar'

'''

