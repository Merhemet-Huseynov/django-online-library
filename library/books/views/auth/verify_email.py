from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from books.models.auth.email_verification import VerificationCode
from books.serializers.auth.verify_email import VerifyEmailSerializer

__all__ = ["VerifyEmailView"]

class VerifyEmailView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VerifyEmailSerializer(data=request.data)
        
        if serializer.is_valid():
            return Response({
                "message": "Verification successful!"
                }, status=status.HTTP_200_OK
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
