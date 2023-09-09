from django.shortcuts import render, get_object_or_404
from .models import task
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import taskSerializer

class taskAll(APIView):
    def get(self, request):
        x=task.objects.all()
        cr=taskSerializer(x, many=True)
        return Response(cr.data)
    
class taskDetail(APIView):
    def get(self, request, *args, **kwargs):
        x=get_object_or_404(task, id=kwargs['forid'])
        cr=taskSerializer(x)
        return Response(cr.data)
    
class taskpost(APIView):
    def post(self, request):
        x=request.data
        z=taskSerializer(data=x)
        if z.is_valid():
            z.save()
            return Response(z.data)
        return Response(z.errors)
    
class taskpatch(APIView):
    def patch(self, request, *args, **kwargs):
        x=get_object_or_404(task, id=kwargs['forid'])
        z=taskSerializer(x, data=request.data, partial=True)
        if z.is_valid():
            z.save()
            return Response(z.data)
        return Response(z.errors)
    

class taskput(APIView):
    def put(self, request, *args, **kwargs):
        x=get_object_or_404(task, id=kwargs['forid'])
        z=taskSerializer(x, data=request.data)
        if z.is_valid():
            z.save()
            return Response(z.data)
        return Response(z.errors)
    

class taskdelete(APIView):
    def delete(self, request, *args, **kwargs):
        x=get_object_or_404(task, id=kwargs['forid'])
        x.delete()
        return Response({"message":"succesfully deleted"})

        













    
    
