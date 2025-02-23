import logging
from rest_framework.views import APIView, Response, status
from drf_yasg.utils import swagger_auto_schema

from accounts.serializers.verification import SendVerificationCodeSerializer
from accounts.models.verification import DailyMessage
from accounts.tasks import send_verification_email


__all__ = ["SendVerificationCodeView"]

logger = logging.getLogger(__name__)


class SendVerificationCodeView(APIView):

    @swagger_auto_schema(request_body=SendVerificationCodeSerializer)
    def post(self, request):
        logger.info(
            "Send verification code request received for email: %s", 
            request.data.get("email")) 

        serializer = SendVerificationCodeSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            logger.info("Email validated: %s", email)

            message_response = DailyMessage.send_message(email)

            if message_response != "Message sent successfully!":
                logger.warning(
                    "Too many requests for email: %s. Response: %s", 
                    email,
                    message_response
                )

                return Response(
                    {"error": message_response},
                    status=status.HTTP_429_TOO_MANY_REQUESTS
                )

            send_verification_email.delay(email)
            logger.info("Verification code sent to email: %s", email)

            return Response(
                {"message": "Verification code sent."},
                status=status.HTTP_200_OK
            )

        logger.error(
            "Invalid data provided: %s",
            serializer.errors
        )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )