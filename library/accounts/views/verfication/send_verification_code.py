from rest_framework.views import APIView, Response, status

from accounts.serializers.verification import SendVerificationCodeSerializer
from accounts.models.verification import DailyMessage
from accounts.tasks import send_verification_email

__all__ = ["SendVerificationCodeView"]


class SendVerificationCodeView(APIView):
    def post(self, request):
        serializer = SendVerificationCodeSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]

            if not DailyMessage.send_message(email):
                return Response(
                    {"error": "Daily message limit reached."},
                    status=status.HTTP_429_TOO_MANY_REQUESTS
                )

            send_verification_email.delay(email)

            return Response(
                {"message": "Verification code sent."},
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
