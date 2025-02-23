import logging
from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from accounts.serializers.password import ChangePasswordSerializer

__all__ = ["ChangePasswordView"]

logger = logging.getLogger(__name__) 


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ChangePasswordSerializer)
    def post(self, request):
        logger.info(
            "Password change request received for user: %s", 
            request.user.email
        )

        serializer = ChangePasswordSerializer(
            data=request.data, 
            context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            logger.info(
                "Password changed successfully for user: %s", 
                request.user.email
            ) 
            return Response({
                "message": "Password changed successfully."
            }, status=status.HTTP_200_OK)
        
        logger.warning(
            "Password change failed for user: %s. Errors: %s", 
            request.user.email, 
            serializer.errors
        )  
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
