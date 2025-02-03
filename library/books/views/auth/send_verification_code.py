from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books.serializers.auth.send_verification_code import SendVerificationCodeSerializer
from books.tasks import send_verification_email

__all__ = ["SendVerificationCodeView"]

class SendVerificationCodeView(APIView):
    def post(self, request):
        serializer = SendVerificationCodeSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            send_verification_email.delay(email)
            return Response({
                "message": "Verification code sent."
                }, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
