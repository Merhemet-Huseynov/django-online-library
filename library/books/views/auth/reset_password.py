# books/views/auth/reset_password.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books.serializers.auth.reset_password import ResetPasswordSerializer

__all__ = ["ResetPasswordView"]

class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            # We update the password by calling the save method of the serializer
            user = serializer.save()
            return Response({
                "message": "Password reset successful."
                }, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
