import logging
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

__all__ = ["LogoutView"]

logger = logging.getLogger(__name__)  


class LogoutView(APIView):
    def post(self, request):
        logger.info("Logout request received")
        
        refresh_token = request.data.get("refresh")
        
        if not refresh_token:
            logger.warning("No refresh token provided") 
            return Response({
                "detail": "Refresh token is required."
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            logger.info("User logged out successfully, token blacklisted") 
            return Response({
                "detail": "Successfully logged out."
            }, status=status.HTTP_200_OK)

        except TokenError:
            logger.error("Invalid token received: %s", refresh_token)  
            return Response({
                "detail": "Invalid token."
            }, status=status.HTTP_400_BAD_REQUEST)
