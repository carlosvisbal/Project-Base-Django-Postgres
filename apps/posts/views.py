from django.http import HttpResponse
from django.views.generic.base import View


class HelloWorld(View):

    def get(self, request):
        return  HttpResponse(content='Hola bebe')
