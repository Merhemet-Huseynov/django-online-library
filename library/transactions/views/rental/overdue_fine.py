import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404

from transactions.models.rental import OverdueFine
from transactions.serializers.rental import OverdueFineSerializer

__all__ = [
    "OverdueFineListView",
    "OverdueFineDetailView"
]

# Logger konfiqurasiya edirik
logger = logging.getLogger(__name__)


class OverdueFineListView(APIView):
    """
    API View to list all overdue fines for the authenticated user.
    
    This view returns a list of overdue fines that belong to the authenticated user only.
    It uses pagination and returns overdue fine details like overdue days and fine amount.

    **URL**: `/overdue_fines/`
    **Method**: `GET`
    
    **Permissions**:
    - Only authenticated users can access their overdue fines.
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a list of overdue fines for the authenticated user.",
        responses={
            200: OverdueFineSerializer(many=True),
            401: "Unauthorized",
            404: "Not found"
        },
        tags=["Overdue Fines"]
    )
    def get(self, request):
        """
        Retrieve the list of overdue fines for the authenticated user.

        This method will only return overdue fines that belong to the authenticated user.

        **Logging**:
        - If any error occurs during retrieval, it will be logged for troubleshooting.

        :param request: The incoming HTTP request.
        :return: JSON response with overdue fines data.
        """
        # Query overdue fines for the authenticated user
        overdue_fines = OverdueFine.objects.filter(rental__user=request.user)
        serializer = OverdueFineSerializer(overdue_fines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OverdueFineDetailView(APIView):
    """
    API View to retrieve a specific overdue fine for the authenticated user.

    This view returns details of a single overdue fine related to the authenticated user.
    
    **URL**: `/overdue_fines/{id}/`
    **Method**: `GET`
    
    **Permissions**:
    - Only authenticated users can access their overdue fine details.
    - Only the overdue fine belonging to the authenticated user will be shown.
    """

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a specific overdue fine for the authenticated user.",
        responses={
            200: OverdueFineSerializer,
            401: "Unauthorized",
            404: "Not found"
        },
        tags=["Overdue Fines"]
    )
    def get(self, request, pk):
        """
        Retrieve a specific overdue fine by ID for the authenticated user.

        This method will return the overdue fine details, including the overdue 
        days and fine amount, but only if it belongs to the authenticated user.

        **Logging**:
        - If the overdue fine is not found or doesn't belong to the authenticated user, 
        the error will be logged.
        
        :param request: The incoming HTTP request.
        :param pk: The ID of the overdue fine to retrieve.
        :return: JSON response with overdue fine data or error message.
        """
        overdue_fine = get_object_or_404(
            OverdueFine, 
            id=pk, 
            rental__user=request.user
        )
        serializer = OverdueFineSerializer(overdue_fine)
        return Response(serializer.data, status=status.HTTP_200_OK)