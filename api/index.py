from application import app
from vercel_wsgi import handle_request

def handler(request):
    return handle_request(app, request)
