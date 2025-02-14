from rest_framework.views import APIView, Response, status
from accounts.serializers.password import ResetPasswordSerializer

__all__ = ["ResetPasswordView"]


class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(
            data=request.data
        )

        if serializer.is_valid():
            user = serializer.save()

            return Response({
                "message": "Password reset successful."
                }, status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
