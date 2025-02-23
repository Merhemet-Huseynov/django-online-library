import logging
from rest_framework.views import APIView, Response, status
from accounts.serializers.auth import LoginSerializer

__all__ = ["LoginView"]

logger = logging.getLogger(__name__)  


class LoginView(APIView):
    def post(self, request):
        logger.info("Login request received")  

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            logger.info("Login successful") 
            return Response(
                serializer.validated_data, 
                status=status.HTTP_200_OK
            )
        
        logger.warning("Login failed: %s", serializer.errors) 
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
