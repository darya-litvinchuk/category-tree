from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from category.api.base.serializers.category import (
    CategorySerializer,
    PostCategorySerializer,
)
from category.exceptions import ServiceException
from category.services.category import CategoryService


class CategoryListView(APIView):
    @staticmethod
    def post(request):
        """
        Creates category tree in the DB.
        POST categories/
        """

        serializer = PostCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            result = CategoryService.create(serializer.validated_data)
        except ServiceException as exception:
            return Response(exception.msg, status=HTTPStatus.BAD_REQUEST)
        serializer = CategorySerializer(result, many=True)
        return Response(serializer.data)
