from dataclasses import dataclass
from typing import List

from category.models import Category


@dataclass
class CategoryDTO:
    id: int
    name: str
    parents: List[Category]
    children: List[Category]
    siblings: List[Category]
