from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers.password import ResetPasswordSendCodeSerializer

__all__ = ["ResetPasswordSendCodeView"]

class ResetPasswordSendCodeView(APIView):
    def post(self, request):
        serializer = ResetPasswordSendCodeSerializer(data=request.data)
        if serializer.is_valid():
            response_data = serializer.save() 
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
