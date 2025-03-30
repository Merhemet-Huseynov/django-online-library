import logging
from rest_framework.views import APIView, Response, status
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from accounts.serializers.auth import RegisterSerializer


__all__ = ["RegisterView"]

logger = logging.getLogger(__name__) 


class RegisterView(APIView):

    @swagger_auto_schema(
        operation_summary="User Registration",
        operation_description="Registers a new user by providing user details (username, email, password, etc.).",
        request_body=RegisterSerializer,
        responses={
            201: openapi.Response(
                description="Registration successful, user created",
                examples={
                    "application/json": {
                        "message": "Registration successful."
                    }
                }
            ),
            400: openapi.Response(
                description="Bad request, invalid registration data",
                examples={
                    "application/json": {
                        "username": ["This field is required."],
                        "email": ["This field is required."],
                        "password": ["This field is required."]
                    }
                }
            ),
        },
        tags=["UserRegister"]
    )
    def post(self, request):
        logger.info("Registration request received with data: %s", request.data)  

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            logger.info("Registration successful for user: %s", user.username) 
            return Response({
                "message": "Registration successful."
                }, status=status.HTTP_201_CREATED
            )

        logger.warning("Registration failed: %s", serializer.errors)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
