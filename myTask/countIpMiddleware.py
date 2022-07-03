from django.http import HttpResponseForbidden
from django.core.cache import cache

class CountIpAddress(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = self.get_response(request)
        
        bronze={}
        silver={}
        gold={'127.0.0.1'}

        ip = request.META['REMOTE_ADDR']
        
        if ip in bronze:
            limit=2
        elif ip in silver:
            limit=5
        elif ip in gold:
            limit=10
        else:
            limit=1
            
        if ip not in cache:
            cache.set(ip,limit,timeout=60)
            return response
        elif cache.get(ip)>0:
            cache.set(ip,cache.get(ip)-1,timeout=60)
            return response
        elif cache.get(ip)==0:
            return HttpResponseForbidden("Please wait for 1 minute to access")
        


    

        
        