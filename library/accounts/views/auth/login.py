from rest_framework.views import APIView, Response, status
from accounts.serializers.auth import LoginSerializer

__all__ = ["LoginView"]


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(
            data=request.data
        )
        
        if serializer.is_valid():
            return Response(
                serializer.validated_data, 
                status=status.HTTP_200_OK
            )
            
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
