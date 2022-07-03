import logging

class GetIpAddress(object):
    def __init__(self,get_response):
        self.get_response = get_response
             
    def __call__(self,request):
        response = self.get_response(request)
        logger = logging.getLogger("django-request")
        logger.info(request.META['REMOTE_ADDR'])
        return response

        