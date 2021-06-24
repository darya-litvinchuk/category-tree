from dataclasses import asdict
from typing import List

from django.db import IntegrityError

from category.exceptions import DuplicationException, NotFoundException
from category.models.category import Category
from category.services.mptt import TreeNode


class CategoryRepository:
    @staticmethod
    def create(category_nodes: List[TreeNode]) -> List[Category]:
        categories = [Category(**asdict(category)) for category in category_nodes]
        try:
            result = Category.objects.bulk_create(categories)
        except IntegrityError:
            raise DuplicationException()
        return result

    @staticmethod
    def by_id(category_id: int) -> Category:
        try:
            result = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            raise NotFoundException(category_id)
        return result

    @staticmethod
    def parents(category: Category) -> List[Category]:
        return Category.objects.filter(left__lt=category.left, right__gt=category.right)

    @staticmethod
    def children(category: Category) -> List[Category]:
        return Category.objects.filter(parent_name=category.name)

    @staticmethod
    def siblings(category: Category) -> List[Category]:
        return Category.objects.filter(parent_name=category.parent_name).exclude(
            pk=category.pk
        )
