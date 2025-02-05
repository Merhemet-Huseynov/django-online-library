from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books.serializers.auth.change_password import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated

__all__ = ["ChangePasswordView"]

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, 
            context={"request": request}
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Password changed successfully."
            }, status=status.HTTP_200_OK
        )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
