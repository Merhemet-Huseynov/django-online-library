from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from books.tasks import send_verification_email
from books.serializers.auth.register import RegisterSerializer

__all__ = ["RegisterView"]

class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            # A new user is created, using email as username
            user = User.objects.create_user(
                username=email, 
                email=email, 
                password=password
            )

            # Sending confirmation email
            send_verification_email(user.id)

            return Response({
                "message": "Registration successful. Please check your email for verification."
                },status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
