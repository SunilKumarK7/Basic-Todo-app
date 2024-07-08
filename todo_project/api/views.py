from rest_framework import generics, permissions
from api.models import ToDo
from api.serializers import ToDoSerializer,UserSerializer
from rest_framework import authentication,permissions
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

class UserCreationView(APIView):

    def post(self,request,*args,**kwargs):

        serializer_instance=UserSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
class TodoCreateView(ModelViewSet):
    serializer_class=ToDoSerializer
    queryset=ToDo.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

