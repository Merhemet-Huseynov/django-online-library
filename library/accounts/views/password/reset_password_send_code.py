import logging
from rest_framework.views import APIView, Response, status
from drf_yasg.utils import swagger_auto_schema

from accounts.serializers.password import ResetPasswordSendCodeSerializer

__all__ = ["ResetPasswordSendCodeView"]

logger = logging.getLogger(__name__) 


class ResetPasswordSendCodeView(APIView):

    @swagger_auto_schema(request_body=ResetPasswordSendCodeSerializer)
    def post(self, request):
        logger.info(
            "Password reset request received for email: %s", 
            request.data.get("email")
        )

        serializer = ResetPasswordSendCodeSerializer(data=request.data)

        if serializer.is_valid():
            response_data = serializer.save()
            logger.info(
                "Password reset code sent successfully to email: %s", 
                request.data.get("email")
            )

            return Response(
                response_data, 
                status=status.HTTP_200_OK
            )

        logger.warning(
            "Password reset failed: %s", 
            serializer.errors
        )
        
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
