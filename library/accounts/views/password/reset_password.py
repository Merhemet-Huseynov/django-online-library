import logging
from rest_framework.views import APIView, Response, status
from accounts.serializers.password import ResetPasswordSerializer

__all__ = ["ResetPasswordView"]

logger = logging.getLogger(__name__) 


class ResetPasswordView(APIView):
    def post(self, request):
        logger.info("Password reset request received")  

        serializer = ResetPasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            logger.info(
                f"Password reset successful for user: {user.email}"
            ) 

            return Response({
                "message": "Password reset successful."
            }, status=status.HTTP_200_OK)

        logger.warning(
            f"Password reset failed: {serializer.errors}"
        )

        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
