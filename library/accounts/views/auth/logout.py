from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

__all__ = ["LogoutView"]


class LogoutView(APIView):
    def post(self, request):
        try:
            # We get the refresh token sent by the user
            refresh_token = request.data.get("refresh")
            
            if not refresh_token:
                return Response({
                    "detail": "Refresh token is required."
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            
            # Blacklist the token
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({
                "detail": "Successfully logged out."
                }, status=status.HTTP_200_OK
            )

        except TokenError:
            return Response({
                "detail": "Invalid token."
                }, status=status.HTTP_400_BAD_REQUEST
            )
