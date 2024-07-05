
from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework.views import APIView
from app.serializers import *
from rest_framework.response import Response

class ProductCrud(APIView):
    def get(self,request,pk):
        LPO=Product.objects.all()
        MSPO=ProductMS(LPO,many=True)
        return Response(MSPO.data)
    
    def post(self,request,pk):
        rjd=request.data
        PDO=ProductMS(data=rjd)
        if PDO.is_valid():
            PDO.save()
            return Response({'success':'Data is inserted successfully.'})
        else:
            return Response({'Failed':'Issues while inserting.'})
        
    def put(self,request,pk):
        instance = Product.objects.get(pk=pk)
        LPO = ProductMS(instance,data=request.data)
        if LPO.is_valid():
            LPO.save()
            return Response({'update':'Data is updated.'})
        else:
            return Response({'fail':'Data is failed to update.'})
    
    def patch(self,request,pk):
        instance = Product.objects.get(pk=pk)
        LPO = ProductMS(instance,data=request.data,partial=True)
        if LPO.is_valid():
            LPO.save()
            return Response({'update':'Data is updated.'})
        else:
            return Response({'fail':'Data is failed to update.'})
    
    def delete(self,request,pk):
        instance = Product.objects.get(pk=pk).delete()
        return Response({'delete':'is success'})
        





        



























        

