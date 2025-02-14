from rest_framework.views import APIView, Response, status
from rest_framework.permissions import IsAuthenticated

from accounts.serializers.password import ChangePasswordSerializer

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
        
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
