from http import HTTPStatus

from rest_framework.response import Response
from rest_framework.views import APIView

from category.api.base.serializers.category import GetCategorySerializer
from category.exceptions import ServiceException
from category.services.category import CategoryService


class CategoryDetailView(APIView):
    @staticmethod
    def get(request, category_id):
        """
        Endpoint retrieves category name, parents (and their parents), children and
        siblings.
        GET categories/:id/
        """
        try:
            category_dto = CategoryService.by_id(category_id)
        except ServiceException as exception:
            return Response(exception.msg, status=HTTPStatus.BAD_REQUEST)
        serializer = GetCategorySerializer(category_dto)
        return Response(serializer.data)
