from rest_framework.response import Response
from rest_framework.viwes import exception_handler as drf_exceptions_handler

def exception_handler(exc,context):
    error = "%s %s %s" % (context['views'],context['request'].metgod,exc)
    print(error)
    response = drf_exceptions_handler(exc,context)
    if response is None:
        return Response({
            'error_message':"你猜，我的网是不是炸了？"
        })
    return response