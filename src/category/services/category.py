from typing import Any, Dict, List

from category.dtos import CategoryDTO
from category.models import Category
from category.repositories.category import CategoryRepository
from category.services.mptt import Tree
from category.services.utils import ChildParentService


class CategoryService:
    @staticmethod
    def create(categories: Dict[str, Any]) -> List[Category]:
        child_parent_map = ChildParentService().child_parent_map([categories])
        category_nodes = Tree(child_parent_map).mptt([], [categories])
        return CategoryRepository.create(category_nodes)

    @staticmethod
    def by_id(category_id: int) -> CategoryDTO:
        category = CategoryRepository.by_id(category_id)
        return CategoryDTO(
            id=category.pk,
            name=category.name,
            parents=CategoryRepository.parents(category),
            children=CategoryRepository.children(category),
            siblings=CategoryRepository.siblings(category),
        )
